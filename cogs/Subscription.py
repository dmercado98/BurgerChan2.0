import discord 
import json
from discord.ext import commands

class Subscription(commands.Cog):
    def __init__(self,client):
        self.subscriptions = None
        initSubscriptions(self)
        addSubscription(self,True,'123')
        print(self.subscriptions)
        self.client = client

    @commands.command()
    async def subscribe(self, ctx, sfwFlag):
        sfwFlag = sfwFlag.lower() == "sfw"
        if(sfwFlag):
            await addSfw(self,ctx) 


def writeSubscriptions(self):
    with open('Subscriptions.json','w') as file:
        file.write(json.dumps(self.subscriptions))

def initSubscriptions(self):
    with open('Subscriptions.json') as file:
        self.subscriptions = json.load(file)

async def addNsfw(self,ctx):
    authorId = str(ctx.author.id)
    sfwArray = self.subscriptions[authorId]["nsfw"]
    alreadySubscribed = False
    for entry in sfwArray:
        if entry[1] == ctx.channel.id :
            alreadySubscribed = True
            break
    if not alreadySubscribed :
        sfwArray.append((ctx.guild.id ,ctx.channel.id))
        writeSubscriptions(self)
    else:
        await ctx.channel.send("You are already subscribed silly")

async def addSfw(self,ctx):
    authorId = str(ctx.author.id)
    DirectMessage = self.client.get_cog("DirectMessage")
    await DirectMessage.dmMe(ctx)
    sfwArray = self.subscriptions[authorId]["sfw"]
    alreadySubscribed = False
    for entry in sfwArray:
        if entry[1] == ctx.channel.id :
            alreadySubscribed = True
            break
    if not alreadySubscribed :
        sfwArray.append((ctx.guild.id ,ctx.channel.id))
        writeSubscriptions(self)
    else:
        await ctx.channel.send("You are already subscribed silly")


def addSubscription(self,isNsfw,ctx):
    if ctx in self.subscriptions:
        if isNsfw:
            addNsfw(self,ctx)
        else:
            addSfw(self,ctx)


def setup(client):
    client.add_cog(Subscription(client))