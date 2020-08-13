import discord 
import json
from discord.ext import commands

class Subscription(commands.Cog):
    def __init__(self,client):
        self.subscriptions = {}
        initSubscriptions(self)
        self.client = client

    @commands.command()
    async def subscribe(self, ctx, nsfwFlag):
        if(nsfwFlag.lower() == "nsfw"):
            await addNsfw(self,ctx)
        elif(nsfwFlag.lower() == "sfw"):
            await addSfw(self,ctx)
        elif(nsfwFlag.lower() == "all"):
            await addNsfw(self,ctx)
            await addSfw(self,ctx)
        else:
            ctx.channel.send("Please use one of the flags nsfw or sfw.")

    @commands.command()
    async def sendNoods(self,ctx,*isSfw):
        toAttach = "nothing"
        authorId = str(ctx.author.id)
        if isinstance(ctx.channel,discord.channel.DMChannel):
            if isSfw == () :
                await ctx.channel.send("Make sure you add the flag sfw or nsfw silly.")
                return
            if isSfw[0].lower() == "sfw":
                for subscription in self.subscriptions[authorId]["sfw"]:
                    channelObj = getChannelObj(self,ctx,subscription)
                    if ctx.message.attachments != [] :
                        toAttach = ctx.message.attachments
                        toAttach = await convertAttachments(self,ctx, toAttach)
                        await channelObj.send(ctx.author.display_name+"sent:",files = toAttach)
                    else:
                        await ctx.channel.send("Make sure to add some attachments silly.")
            elif isSfw[0].lower() == "nsfw":
                for subscription in self.subscriptions[authorId]["nsfw"]:
                    channelObj = getChannelObj(self,ctx,subscription)
                    if ctx.message.attachments != [] :
                        toAttach = ctx.message.attachments
                        toAttach = await convertAttachments(self,ctx, toAttach)
                        await channelObj.send(ctx.author.display_name + "sent:",files = toAttach)
                    else:
                        await ctx.channel.send("Make sure to add some attachments silly.")
            else:
                await ctx.channel.send("Make sure you add the flag sfw or nsfw silly.")

def getChannelObj(self, ctx,channelId):
    channelObj = self.client.get_channel(channelId)
    return channelObj

async def convertAttachments(self,ctx,toAttach):
    fileList = []
    for attachment in toAttach:
        fileList.append(await attachment.to_file())
    return fileList

def writeSubscriptions(self):
    with open('Subscriptions.json','w') as file:
        file.write(json.dumps(self.subscriptions))

def initSubscriptions(self):
    with open('Subscriptions.json') as file:
        self.subscriptions = json.load(file)

async def addNsfw(self,ctx):
    authorId = str(ctx.author.id)
    nsfwArray = self.subscriptions[authorId]["nsfw"]
    alreadySubscribed = False
    for entry in nsfwArray:
        if entry == ctx.channel.id :
            alreadySubscribed = True
            break
    if not alreadySubscribed :
        nsfwArray.append(ctx.channel.id)
        writeSubscriptions(self)
    else:
        await ctx.channel.send("You are already subscribed silly")

async def addSfw(self,ctx):
    authorId = str(ctx.author.id)
    if authorId not in self.subscriptions.keys():
        addUser(self,ctx)
    sfwArray = self.subscriptions[authorId]["sfw"]
    alreadySubscribed = False
    for entry in sfwArray:
        if entry == ctx.channel.id :
            alreadySubscribed = True
            break
    if not alreadySubscribed :
        sfwArray.append(ctx.channel.id)
        writeSubscriptions(self)
    else:
        await ctx.channel.send("You are already subscribed silly")


def addSubscription(self,isNsfw,ctx):
    if ctx in self.subscriptions:
        if isNsfw:
            addNsfw(self,ctx)
        else:
            addSfw(self,ctx)

def addUser(self,ctx):
    self.subscriptions[str(ctx.author.id)] = {"sfw":[] , "nsfw" : []}

def setup(client):
    client.add_cog(Subscription(client))