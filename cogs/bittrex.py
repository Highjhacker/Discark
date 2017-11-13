import requests
import discord
import aiohttp
from discord.ext import commands
import os


class Bittrex:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://bittrex.com/api/v1.1/"

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)

    def get_infos(self):
        r = self.get("public/getticker?market=btc-ark")
        infos = r.json()["result"]
        return infos

    def get_last_price(self):
        r = self.get("public/getticker?market=btc-ark")
        last_price = r.json()["result"]["Last"]
        return last_price

    def get_ask_price(self):
        r = self.get("public/getticker?market=btc-ark")
        ask_price = r.json()["result"]["Ask"]
        return ask_price

    def get_bid_price(self):
        r = self.get("public/getticker?market=btc-ark")
        bid_price = r.json()["result"]["Bid"]
        return bid_price

    @commands.command(name="bittrexlast")
    async def say_last_price(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Bittrex", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Last price :", value="{0} BTC".format(self.get_last_price()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="bittrexask")
    async def say_ask_price(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Bittrex", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Ask price :", value="{0} BTC".format(self.get_ask_price()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="bittrexbid")
    async def say_bid_price(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Bittrex", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Bid price :", value="{0} BTC".format(self.get_bid_price()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="bittrexinfo")
    async def say_infos(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Bittrex", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Ask price :", value="{0} BTC".format(self.get_ask_price()))
            embed.add_field(name="Bid price :", value="{0} BTC".format(self.get_bid_price()))
            embed.add_field(name="Last price :", value="{0} BTC".format(self.get_last_price()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid")
            print(e)


def setup(bot):
    bot.add_cog(Bittrex(bot))