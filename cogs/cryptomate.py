import requests
import discord
import json
import arrow
from discord.ext import commands


class Cryptomate:
    def __init__(self, bot):
        self.bot = bot

    def get_ark_info(self, currency=""):
        url = "https://cryptomate.co.uk/api/ARK/{0}".format(currency)
        r = requests.get(url).json()
        return r["ARK"]

    def get_ark_price(self, currency=""):
        r = self.get_ark_info(currency)
        return r["price"]

    @commands.command(name="cryptomateprice")
    async def say_ark_price(self, currency=""):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptomate", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            if currency:
                embed.add_field(name="{0} price :".format(currency.upper()), value="{0}".format(self.get_ark_price(currency), inline=False))
            else:
                embed.add_field(name="USD price :", value="{0}".format(self.get_ark_price(currency), inline=False))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    def get_ark_change(self, currency=""):
        r = self.get_ark_info(currency)
        return r["change"]

    @commands.command(name="cryptomatechange")
    async def say_ark_change(self, currency=""):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptomate", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            if currency:
                if float(self.get_ark_change()) > 0.00:
                    embed.add_field(name="% Change in {0} :".format(currency.upper()), value="{0} % :arrow_up:".format(self.get_ark_change(currency), inline=False))
                else:
                    embed.add_field(name="% Change in {0} :".format(currency.upper()), value="{0} % :arrow_down:".format(self.get_ark_change(currency), inline=False))
            else:
                if float(self.get_ark_change()) > 0.00:
                    embed.add_field(name="% Change in USD :", value="{0} % :arrow_up:".format(self.get_ark_change(currency), inline=False))
                else:
                    embed.add_field(name="% Change in USD :", value="{0} % :arrow_down:".format(self.get_ark_change(currency), inline=False))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    def get_ark_volume(self, currency=""):
        r = self.get_ark_info(currency)
        return r["volume"]

    @commands.command(name="cryptomatevolume")
    async def say_ark_volume(self, currency=""):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptomate", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            if currency:
                embed.add_field(name="Volume in {0} :".format(currency.upper()), value="{0}".format(self.get_ark_volume(currency), inline=False))
            else:
                embed.add_field(name="Volume in USD :", value="{0}".format(self.get_ark_volume(currency), inline=False))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

def setup(bot):
    bot.add_cog(Cryptomate(bot))
