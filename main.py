import discord
from discord.ext import commands
import sys
import os
import traceback
import asyncio
from cogs.coinmarketcap import CoinMarketCap
import requests

"""
Note : The msg can't exceed 2000 chars
"""

description = """ DiscArk : The Ark Ecosystem Discord Bot. Next stop : The moon. """

initial_extensions = [
    'cogs.coinmarketcap',
    'cogs.ark_utils',
    'cogs.bittrex',
]

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), description=description)

async def get_status_price():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
    price = r.json()[0]["price_usd"]
    return price

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def update_bot_status_background():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name="{0} $".format(await get_status_price())))
        await asyncio.sleep(5)


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.loop.create_task(update_bot_status_background())
    bot.run(os.environ.get('DISCORD_PRIVATE_KEY'))