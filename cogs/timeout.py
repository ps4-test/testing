import discord,datetime
from discord.ext import commands

t_error='moderate members'

class TimeOut(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('timeout.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def timeout(self,ctx,member:discord.Member,seconds: int=0,reason=None):
        if ctx.author.id == member.id :
            await ctx.reply('**You cannot timeout yourself!**')

        duration =  datetime.timedelta(seconds=seconds)
        timeout_embed = discord.Embed(title='**User Timedout!**',color=discord.Color.dark_red())
        timeout_embed.add_field(name='**Name of the member:**',value=f'{member.mention}',inline=False)
        timeout_embed.add_field(name='**User ID of the member:**',value=f'{member.id}',inline=False)
        timeout_embed.add_field(name='**Duration of the member:**',value=f'**{duration}**',inline=False)
        timeout_embed.add_field(name='**Reason of the timeout:**',value=f'{reason}',inline=False)
        
        await member.timeout(duration)
        await ctx.reply(embed=timeout_embed)
        
    @timeout.error
    async def timeout_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run kick command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{t_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{t_error}")

            

async def setup(client):
    await client.add_cog(TimeOut(client))
