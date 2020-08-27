import discord 
import webbrowser
from discord.ext import commands


async def sendCard( self, ctx, userID ):
    # Sends a message to the channel that the card was sent and
      # sends the card to the birthday pal with a happy birthday message
    birthdayDM = self.client.get_cog("DirectMessage")
    await birthdayDM.dmSomeone(ctx)

async def signCard(self, ctx, *args):
    # args order: args[0] = the birthday pal
                # args[1:] = people signing
    # check to see if a card's already been started for birthday pal
        # if not, create card
        # sign
    # else add user signature

    # stores birthdays?

async def peekCard(self, ctx, user):
    # searches for birthday card started for the user
    # if started:
        # show who signed the card and when
    # else message "card not found"

class BirthdayCard(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def bdayCard(self, ctx, *args):
        # args order: args[0] = command
                # args[1] = birthday pal
                # **args[2:] = could be people you're signing for
        bdayPal = args[1]

        if args[0].lower() == "sign":
            await signCard( self, ctx, bdayPal, ctx.author.display_name )

        elif args[0].lower() == "send":
            await sendCard( ctx, bdayPal )

        elif args[0].lower() == "peek":
            await peekCard( ctx, bdayPal )


def setup(client):
    client.add_cog(BirthdayCard(client))