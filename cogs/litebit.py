import requests
import discord
import aiohttp
from discord.ext import commands
import os

# Vraiment pas sur du coup avec le embed en constructeur mais on va laisser ça ici et juste pour litebit en guise de test


class Litebit:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://api.litebit.eu/market/ark"
        self.embed = discord.Embed(title="Ark(ARK) - LiteBit", colour=discord.Colour.dark_red())
        self.embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")

    def get(self):
        return requests.get(self.base_url)

    def get_full_info(self):
        r = self.get()
        resp = r.json()["result"]
        return resp

    def get_buy_price(self):
        r = self.get_full_info()
        resp = r["buy"]
        return resp

    @commands.command(name="litebitbuy")
    async def say_buy_price(self):
        self.embed.add_field(name="Buy price :", value="{0} €".format(self.get_buy_price()))
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields() # Empty ?

    def get_sell_price(self):
        r = self.get_full_info()
        resp = r["sell"]
        return resp

    @commands.command(name="litebitsell")
    async def say_sell_price(self):
        self.embed.add_field(name="Sell price :", value="{0} €".format(self.get_sell_price()))
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields()

    def get_abbreviation(self):
        r = self.get_full_info()
        resp = r["abbr"]
        return resp

    @commands.command(pass_context=True)
    async def say_abbreviation(self):
        self.embed.add_field(name="Abbreviation :", value=self.get_abbreviation())
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields()

    def get_name(self):
        r = self.get_full_info()
        resp = r["name"]
        return resp

    @commands.command(pass_context=True)
    async def say_name(self):
        self.embed.add_field(name="Name :", value=self.get_name())
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields()

    def get_volume(self):
        r = self.get_full_info()
        resp = r["volume"]
        return resp

    @commands.command(pass_context=True)
    async def say_volume(self):
        self.embed.add_field(name="Volume :", value=self.get_volume())
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields()

    def get_available(self):
        r = self.get_full_info()
        resp = r["available"]
        return resp

    @commands.command(pass_context=True)
    async def say_available(self):
        self.embed.add_field(name="Abbreviation :", value=self.get_available())
        await self.bot.say(embed=self.embed)
        self.embed.clear_fields()

    @commands.command(name="litebit")
    async def say_full_infos(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - LiteBit", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Name :", value=self.get_name())
            embed.add_field(name="Abbreviation :", value=self.get_abbreviation())
            embed.add_field(name="Buy price :", value="{0} €".format(self.get_buy_price()))
            embed.add_field(name="Sell price :", value="{0} €".format(self.get_sell_price()))
            embed.add_field(name="Volume :", value="{0}".format(self.get_volume()))
            embed.add_field(name="Available :", value="{0}".format(self.get_available()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")


def setup(bot):
    bot.add_cog(Litebit(bot))