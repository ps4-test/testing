import discord 
from discord.ext import commands
import random 

class ChatCogs(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('MyCogs.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    async def Ping(self,ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.reply(f'Pong! {bot_latency}ms.')
    
    @commands.command()
    @commands.guild_only()
    async def RPS(self,ctx):
        rps_list=['rock :rock:','paper :roll_of_paper:','scissors :scissors:']
        result = random.choice(rps_list)
        await ctx.reply(result)
    
    @commands.command()
    @commands.guild_only()
    async def RNG(self,ctx):
        start,end=0,100
        result = random.randint(start,end)
        await ctx.reply(f'The random number from {start} to {end} is {result}')
    
    @commands.command()
    @commands.guild_only()
    async def flip_a_coin(self,ctx):
        flip=['heads','tails']
        result = random.choice(flip)
        await ctx.reply(f'It\'s {result}!')

async def setup(client):
    await client.add_cog(ChatCogs(client))