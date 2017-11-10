import requests
from discord.ext import commands


class Bittrex:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://bittrex.com/api/v1.1/"

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)

    def get_infos(self, first_currency, second_currency):
        r = self.get("public/getticker?market=%s-%s" % (first_currency, second_currency))
        infos = r.json()["result"]
        return infos

    def get_last_price(self, first_currency, second_currency):
        r = self.get("public/getticker?market=%s-%s" % (first_currency, second_currency))
        last_price = r.json()['last']
        return last_price

    def get_ask_price(self, first_currency, second_currency):
        r = self.get("public/getticker?market=%s-%s" % (first_currency, second_currency))
        ask_price = r.json()['ask']
        return ask_price

    def get_bid_price(self, first_currency, second_currency):
        r = self.get("public/getticker?market=%s-%s" % (first_currency, second_currency))
        bid_price = r.json()['bid']
        return bid_price

    @commands.command(name="bittrex last")
    async def say_last_price(self, first_currency, second_currency):
        await self.bot.say(self.get_last_price(first_currency, second_currency))

    @commands.command(name="bittrex ask")
    async def say_ask_price(self, first_currency, second_currency):
        await self.bot.say(self.get_ask_price(first_currency, second_currency))

    @commands.command(name="bittrex bid")
    async def say_ask_price(self, first_currency, second_currency):
        await self.bot.say(self.get_bid_price(first_currency, second_currency))

    @commands.command(name="bittrex info")
    async def say_infos(self, first_currency, second_currency):
        await self.bot.say(self.get_infos(first_currency, second_currency))

def setup(bot):
    bot.add_cog(Bittrex(bot))