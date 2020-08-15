# don't think i need anymore imports
import discord 
from discord.ext import commands
import requests

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
        'search': name 
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    r = requests.post(url, json={'query': query, 'variables': variables})
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
        'search': name 
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    r = requests.post(url, json={'query': query, 'variables': variables})
    print(r.content)
# i think this is all it needs if i remember
class AniFinder( commands.Cog ):
    def __init__( self, client ):
        self.client = client 

    @commands.command()
    async def finder( self, ctx, *args ): # probs not the right parameters?? i'll figure it out later
        print( "Searching AniList for: " + args[1] )
        # figure out if its anime or manga based on flag??
        if args[0] == "MANGA":
            await searchManga( args[0], args[1] )
            print( "Finding " + args[0] + " name..." )
        else: # assuming these are the only two things getting searched
            await searchAnime( args[0], args[1] )
            print( "Finding " + args[0] + " name..." )



def setup(client):
    client.add_cog(AniFinder(client))
