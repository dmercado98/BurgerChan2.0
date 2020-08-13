import discord 
import webbrowser
from discord.ext import commands
    
async def dmSomeone(self,userID):
    userObj = await self.client.fetch_user(userID)
    if userObj.dm_channel == None:
        await userObj.create_dm()
    slideInto = userObj.dm_channel
    await slideInto.send("https://www.youtube.com/watch?v=Nd5ieJcM_Tg")

class DirectMessage(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def dmMe(self,ctx):
        await dmSomeone(self,ctx.author.id)
        print("Dmd " + ctx.author.display_name)

def setup(client):
    client.add_cog(DirectMessage(client))