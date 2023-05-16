import discord
from discord.ext import commands


class Get_Client_Guilds(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    
    
    @commands.command()
    @commands.is_owner()
    async def Get_Client_Guilds(self,ctx):
        await ctx.reply('This may take some time!')
        guilds=[]
        guilds = [guild async for guild in self.client.fetch_guilds(limit=150)]
        return_list=[]
        for x in guilds:
            return_list.append(f'{x}')
        await ctx.reply(f'the guilds are: {return_list}')

    @Get_Client_Guilds.error
    async def Get_Client_Guilds_Error(self,ctx,error):
        if ctx.author.id != 397679536818487296:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!!** \n __only the owner of this bot can use it__ ')
            
