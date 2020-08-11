import discord 
from discord.ext import commands

class RoleUpdate(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(pass_context=True)
    async def acommand(self,ctx):
        await ctx.channel.send("what")

def setup(client):
    client.add_cog(RoleUpdate(client))