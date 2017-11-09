import discord
from discord.ext import commands
import sys
import os
import traceback

"""
Note : The msg can't exceed 2000 chars
"""

description = """ DiscArk : The Ark Ecosystem Discord Bot. Next stop : The moon. """

initial_extensions = [
    'cogs.coinmarketcap'
]

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def wait_until_login():
    await bot.change_presence(game=discord.Game(name="Ark price is MOON$"))

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(os.environ.get('DISCORD_PRIVATE_KEY'))