import discord 
import webbrowser
from discord.ext import commands
from datetime import date


async def birthdayDM(self, userID):
    userObj = await self.client.fetch_user(userID)
    if userObj.dm_channel == None:
        await userObj.create_dm()
    slideInto = userObj.dm_channel
    await slideInto.send("HAPPY BIRTHDAY " + userID.display_name + \
        "https://www.youtube.com/watch?v=oAQmRO42UHc") #birthday vid
    print("HAPPY BIRTHDAY " + userID.display_name + \
        "https://www.youtube.com/watch?v=oAQmRO42UHc")


# stores birthdays
async def storeBirthday( self, ctx, name, date ):
    birthdays = {}
    birthdays[ name ] = date
    print("Stored " + name + "'s birthday: " + date )
    await ctx.channel.send( "Stored " + name + "'s birthday: " + date )

async def getBirthday(self, name):
    print( birthdays[name] )
    await ctx.channel.send( birthdays[name] )

# "$bdayCard send @user"
async def sendCard( self, ctx, user ):
    # Sends a message to the channel that the card was sent and
      # sends the card to the birthday pal with a happy birthday message
    bdayPal = message.mentions[0].id
    await birthdayDM.dmSomeone( bdayPal )
    await ctx.channel.send( ctx.author.display_name + " sent a birthday card to " + \
        bdayPal.display_name + "from " + cards[user][0:] )

async def signCard(self, ctx, *args):
    # args order: args[0] = the birthday pal
                # args[1:] = people signing
   
    cards = {}
    bdayPal = args[0]
    signatures = " ".join( args[1:] )
     # check to see if a card's already been started for birthday pal
        # if not, create card and sign
    if bdayPal not in cards:
        cards[ bdayPal ][0:] = signatures

    else:
        # add signatures
        cards[ bdayPal ].append( signatures )

async def peekCard(self, ctx, user):
    # searches for birthday card started for the user
    # if started:
        # show who signed the card (and when?)
    signatures = " ".join( args[0:] )
    if user in cards:
        await ctx.channel.send( cards[user][signatures] )

    # else message "card not found"
    else:
        await ctx.channel.send( "Card not found" )

class BirthdayCard(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def bdayCard(self, ctx, *args):
        # args order: args[0] = command
                # args[1] = birthday pal
                # **args[2:] = could be people you're signing for
        # bdayPal = args[1]
        bdayPal = ctx.message.mentions[0].id

        if args[0].lower() == "dm":
            birthdayDM(bdayPal)

        elif args[0].lower() == "sign":
            await signCard( self, ctx, bdayPal, ctx.author.display_name )

        elif args[0].lower() == "send":
            await sendCard( ctx, bdayPal )

        elif args[0].lower() == "peek":
            await peekCard( ctx, bdayPal )

        elif args[0].lower() == "store":
            date = " ".join( args[2:] )
            await storeBirthday( ctx, bdayPal, date )
        
        else:
            args[0].lower() == "birthday":
            await getBirthday( bdayPal )


def setup(client):
    client.add_cog(BirthdayCard(client))
