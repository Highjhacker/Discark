import requests
import discord
import json
import arrow
from discord.ext import commands


class Cryptopia:
    def __init__(self, bot):
        self.bot = bot

    def getArkPriceFromCryptoCompare(self, *args):
        url = "https://min-api.cryptocompare.com/data/price?fsym=ARK&tsyms="
        try:
            for currency in args:
                url += currency.upper() + ','
            r = json.loads(requests.get(url[:-1]).text)
            return r
        except requests.ConnectionError:
            return 1

    @commands.command(name="ccprice")
    async def say_price(self, *args):
        try:
            embed = discord.Embed(title="Ark(ARK) - CryptoCompare", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            for currency in args:
                embed.add_field(name="{0} price :".format(currency.upper()), value="{0}".format(self.getArkPriceFromCryptoCompare(currency), inline=False))
            if len(args) == 0:
                await self.bot.say("You need to specify an other (crypto)currency to convert it !")
            else:
                await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    def get_historical_ark_price(self, timestamp, *args):
        corrected_timestamp = arrow.get(timestamp, 'MM/DD/YY').timestamp
        url = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=ARK&ts={0}&tsyms=".format(corrected_timestamp)
        try:
            for currency in args:
                url += currency.upper() + ','
            r = json.loads(requests.get(url[:-1]).text)
            return r
        except requests.ConnectionError:
            return 1

    @commands.command(name="cchistoric")
    async def say_historical_ark_price(self, timestamp, *args):
        try:
            embed = discord.Embed(title="Ark(ARK) - CryptoCompare", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Date :", value=arrow.get(timestamp, 'MM/DD/YY').humanize())
            for currency in args:
                embed.add_field(name="Price :", value=self.get_historical_ark_price(timestamp, currency), inline=False)
            if len(args) == 0:
                await self.bot.say("You need to specify a valid date (MM/DD/YY) and (crypto)currency.")
            else:
                await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

def setup(bot):
    bot.add_cog(Cryptopia(bot))
