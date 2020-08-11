import discord 
from discord.ext import commands

class Subscription(commands.Cog):
    def __init__(self,client):
        self.subscriptions = {123:{"name":"tzona", "sfw":[1,2,3],"nsfw":[1,2,3]}}
        self.client = client

def initSubscriptions(self):
    print('what')
def writeSubscriptions(self):
    print('yeah')

def setup(client):
    client.add_cog(Subscription(client))