import discord
import requests
from discord.ext import commands
import arrow


class Bittrex:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://api.coinmarketcap.com/v1/ticker/"

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)


def setup(bot):
    bot.add_cog(Bittrex(bot))