import discord
import requests
from discord.ext import commands
import arrow
from datetime import datetime


class CoinMarketCap:
    def __init__(self, bot):
        self.bot = bot

    def get_full_infos(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")

        return r.json()[0]#json.dumps(r.json()[0], indent=4, sort_keys=True)

    def get_price(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        price = r.json()[0]["price_usd"]
        return price

    def get_volume_usd(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        volume = r.json()[0]["24h_volume_usd"]
        return volume

    def get_available_supply(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        available_supply = r.json()[0]["available_supply"]
        return available_supply

    def get_id(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        id = r.json()[0]["id"]
        return id

    def get_last_updated(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        last_updated = r.json()[0]["last_updated"]
        return arrow.Arrow.fromtimestamp(last_updated).humanize()

    def get_market_cap(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        market_cap = r.json()[0]["market_cap_usd"]
        return market_cap

    def get_max_supply(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        max_supply = r.json()[0]["max_supply"]
        return max_supply

    def get_name(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        name = r.json()[0]["name"]
        return name

    def get_percent_change_one_hour(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        price = r.json()[0]["percent_change_1h"]
        return price

    def get_percent_change_day(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        price = r.json()[0]["percent_change_24h"]
        return price

    def get_percent_change_week(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        price = r.json()[0]["percent_change_7d"]
        return price

    def get_price_btc(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        price = r.json()[0]["price_btc"]
        return price

    def get_rank(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        rank = r.json()[0]["rank"]
        return rank

    def get_symbol(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        symbol = r.json()[0]["symbol"]
        return symbol

    def get_total_supply(self):
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
        total_supply = r.json()[0]["total_supply"]
        return total_supply

    @commands.command(name="infos")
    async def say_infos(self):
        try:
            embed = discord.Embed(title="Ark(Ark) - CoinMarketCap full informations", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Name", value=self.get_name(), inline=False)
            embed.add_field(name="Symbol", value=self.get_symbol(), inline=False)
            embed.add_field(name="Rank", value=self.get_rank(), inline=False)
            embed.add_field(name="ID", value=self.get_id(), inline=False)

            embed.add_field(name="Price", value=self.get_price() + " $", inline=False)
            embed.add_field(name="Price (BTC)", value=self.get_price_btc() + " BTC", inline=False)

            embed.add_field(name="Volume (24h)", value=self.get_volume_usd() + " $", inline=False)
            embed.add_field(name="Market Cap", value=self.get_market_cap() + "$", inline=False)

            embed.add_field(name="Circulating supply", value=self.get_available_supply(), inline=False)
            embed.add_field(name="Max supply", value=self.get_max_supply(), inline=False)
            embed.add_field(name="Total supply", value=self.get_total_supply(), inline=False)

            embed.add_field(name="% change (1h)", value=self.get_percent_change_one_hour() + " %", inline=False)
            embed.add_field(name="% change (24h)", value=self.get_percent_change_day() + " %", inline=False)
            embed.add_field(name="% change (7days)", value=self.get_percent_change_week() + " %", inline=False)

            embed.add_field(name="Last update", value=self.get_last_updated(), inline=False)

            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="price")
    async def say_price(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - CoinMarketCap", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Current price :", value=self.get_price() + " $")
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")


def setup(bot):
    bot.add_cog(CoinMarketCap(bot))