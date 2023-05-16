

class SetupHelp(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('SetupHelp.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def Setup(self,ctx):
        setup_embed = discord.Embed(title=f'{self.client.user} **Setup!**',description=f'Set log-channel as a private channel and give permissions to {self.client.user}',color=discord.Color.light_grey())
        setup_embed.add_field(name='**Roles and Permission for this bot:**',value=f'{req_perm_role}',inline=False)
        await ctx.send(embed=setup_embed)
    
    @Setup.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s)")

req_perm_role = '''**__Kick Member\nBan Member\nManage Messages\nAdministartor (for your self)\nMake #log-channel a private channel for only admin\staff__**'''

