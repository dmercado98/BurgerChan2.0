import discord 
from discord.ext import commands

class VoiceClient(commands.Cog):
    def __init__(self,client):
        self.discordVoiceClient = None
        self.client = client
    
    @commands.command(pass_context = True)
    async def join(self, message):
        userId = message.author.id
        guild = message.guild
        guildVoice = guild.voice_channels
        for voiceChannel in guildVoice:
            for vcMembers in voiceChannel.members:
                if vcMembers.id == userId:
                    self.discordVoiceClient = await voiceChannel.connect()
                    break

    @commands.command(pass_context = True)
    async def leavePls(self,ctx):
        if self.discordVoiceClient != None:
            await self.discordVoiceClient.disconnect()
            self.discordVoiceClient = None
        else:
            await ctx.channel.send("its not in a voice chat silly")

def setup(client):
    client.add_cog(VoiceClient(client))