# don't think i need anymore imports
import discord 
from discord.ext import commands

# just for searching anime
async def searchManga( self, media, name ):
    query = '''

    query( $page:Int, $perPage:Int, $search:Str )
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
            media( $search:$search, type:MANGA )
            {
                Found: siteUrl
            }
        }
    }
    '''
    # also can you put strings inside queries to print?
    # I do Found: siteUrl and it seemed to work in Postman but idk
    # questions for later i guess lol

    variables = 
    {
        'search': title 
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})

# just searches anime
async def searchAnime(self, media, name):
    query = '''

    query( $page:Int, $perPage:Int, $search:Str )
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
            media( $search:$search, type:MANGA )
            {
                Found: siteUrl
            }
        }
    }
    '''
    
    variables = 
    {
        'search': title 
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})

# i think this is all it needs if i remember
class AniFinder( commands.Cog ):
    def __init__( self, client ):
        self.client = client

    @commands.command()
    async def finder( self, media, name ): # probs not the right parameters?? i'll figure it out later
        print( "Searching AniList for: " + media )
        # figure out if its anime or manga based on flag??
            if media == MANGA:
                await searchManga( self, media, name )
                print( "Finding " + media + " name..." )
            else: # assuming these are the only two things getting searched
                await searchAnime( self, media, name )
                print( "Finding " + media + " name..." )

searchManga( MANGA, nisekoi )
searchAnime( ANIME, my hero academia ) 

def setup(client):
    client.add_cog(AniFinder(client))
