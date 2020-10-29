import discord
import asyncio
import json
import requests
import platform
from discord.ext import commands
from apiKey import apiKey
import os

client = commands.Bot(command_prefix='$')
@client.event
async def on_ready():
    print('Logged on as {0}'.format(client.user))
    
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(extension)

@client.command()
async def reloadAll(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.reload_extension(f'cogs.{filename[:-3]}')
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename[:-3]}')

client.run(apiKey)
