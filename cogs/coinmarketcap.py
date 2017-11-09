import requests
from discord.ext import commands
import json


class CoinMarketCap:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def get_price(self):
        try:
            r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
            price = r.json()[0]["price"]
            await self.bot.say(price)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")


def setup(bot):
    bot.add_cog(CoinMarketCap(bot))