# don't think i need anymore imports
import discord 
from discord.ext import commands
import requests
import sys
import aiohttp

# just for searching anime
async def searchManga( media, name ):
    query = '''

    query( $page:Int, $perPage:Int, $search:String )
    {
        Page ( page:$page, perPage:$perPage )
        {
            pageInfo
            {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media( search:$search, type:MANGA )
            {
                Found: siteUrl
            }
        }
    }
    '''
    # also can you put strings inside queries to print?
    # I do Found: siteUrl and it seemed to work in Postman but idk
    # questions for later i guess lol

    variables = {
        'search': name,
        'page': 1,
        'perPage': 3 
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    # r = requests.post(url, json={'query': query, 'variables': variables})

        # gives a syntax error?? just tryin to make the request asynchronously
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={'query': query, 'variables': variables})
    print(r.content)
# just searches anime
async def searchAnime( media, name ):
    query = '''

    query( $page:Int, $perPage:Int, $search:String )
    {
        Page ( page:$page, perPage:$perPage )
        {
            pageInfo
            {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media( search:$search, type:MANGA )
            {
                Found: siteUrl
            }
        }
    }
    '''
    
    variables = {
        'search': name,
        'page': 1,
        'perPage': 3
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    #r = requests.post(url, json={'query': query, 'variables': variables})
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={'query': query, 'variables': variables})
    print(r.content)

class AniFinder( commands.Cog ):
    def __init__( self, client ):
        self.client = client
        self.request = None

    @commands.command()
    async def finder( self, ctx, *args ):
        # to grab all the words in the title
        title = " ".join( args[1:] )
        print( "Searching AniList for: " + title )
        print( "Finding " + args[0] + " name..." )

        if args[0].lower() == "manga":        
            # it's still not saving the request
            self.request = await searchManga( args[0], title )
            
            await ctx.channel.send( self.request.content )

        elif args[0].lower() == "anime":
            self.request = await searchAnime( args[0], title )
            # send message to channel
            await ctx.channel.send( self.request.content )
            
        else:
            print( "Please include the \"anime\" or \"manga\" flag before the title" )
            await ctx.channel.send( "Please include the \"anime\" or \"manga\" flag before the title" )



def setup(client):
    client.add_cog(AniFinder(client))
