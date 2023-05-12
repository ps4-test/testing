import discord
from discord.ext import commands,tasks
from itertools import cycle
import os
import asyncio

c_prefix='.$'
TOKEN='your_token'

client = commands.Bot(command_prefix=f'{c_prefix}',intents=discord.Intents.all())

client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user} is online!')
    print('==========================')
    change_status.start()

bot_status = cycle([f'{c_prefix}help'])

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

async def load():
    for filename in os.listdir("path_of_the_folder_named_cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())
