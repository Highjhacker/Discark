import requests
import discord
from discord.ext import commands


class Cryptopia:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://www.cryptopia.co.nz/api/GetMarket/ARK_BTC"

    def get(self):
        return requests.get(self.base_url)

    def get_all(self):
        response = self.get().json()
        return response['Data']

    def get_close_price(self):
        response = self.get_all()
        return response['Close']

    def get_ask_price(self):
        response = self.get_all()
        return response['AskPrice']

    def get_low_price(self):
        response = self.get_all()
        return response['Low']

    def get_high_price(self):
        response = self.get_all()
        return response['High']

    def get_last_price(self):
        response = self.get_all()
        return response['LastPrice']

    def get_open_price(self):
        response = self.get_all()
        return response['Open']

    def get_bid_price(self):
        response = self.get_all()
        return response['BidPrice']

    def get_change(self):
        response = self.get_all()
        return response['Change']

    def get_sell_volume(self):
        response = self.get_all()
        return response['SellVolume']

    def get_sell_base_volume(self):
        response = self.get_all()
        return response['SellBaseVolume']

    def get_buy_volume(self):
        response = self.get_all()
        return response['BuyVolume']

    def get_buy_base_volume(self):
        response = self.get_all()
        return response['BuyBaseVolume']

    def get_base_volume(self):
        response = self.get_all()
        return response['BaseVolume']

    def get_volume(self):
        response = self.get_all()
        return response['Volume']

    def get_label(self):
        response = self.get_all()
        return response['Label']

    def get_trade_pair_id(self):
        response = self.get_all()
        return response['TradePairId']

    @commands.command(name="cryptopiafull")
    async def say_cryptopia_full_informations(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptopia", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Open price :", value="{0} BTC".format(self.get_open_price(), inline=True))
            embed.add_field(name="Close price :", value="{0} BTC".format(self.get_close_price(), inline=True))

            embed.add_field(name="Low price :", value="{0} BTC".format(self.get_low_price(), inline=True))
            embed.add_field(name="High price :", value="{0} BTC".format(self.get_high_price(), inline=True))

            embed.add_field(name="Ask price :", value="{0} BTC".format(self.get_ask_price(), inline=False))
            embed.add_field(name="Last price :", value="{0} BTC".format(self.get_last_price(), inline=False))
            embed.add_field(name="Bid price :", value="{0} BTC".format(self.get_bid_price()))
            if float(self.get_change()) > 0.00:
                embed.add_field(name="Change :", value="{0} % :arrow_up:".format(self.get_change()))
            else:
                embed.add_field(name="Change :", value="{0} % :arrow_down:".format(self.get_change()))
            embed.add_field(name="Volume (sell) :", value=self.get_sell_volume())
            embed.add_field(name="Base Volume (sell) :", value=self.get_sell_base_volume())
            embed.add_field(name="Base Volume :", value=self.get_base_volume())
            embed.add_field(name="Volume :", value=self.get_volume())
            embed.add_field(name="Volume (buy):", value=self.get_buy_volume())
            embed.add_field(name="Base Volume (buy):", value=self.get_buy_base_volume())
            embed.add_field(name="Label :", value=self.get_label())
            embed.add_field(name="Trade pair ID :", value=self.get_trade_pair_id())

            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="cryptopiavolume")
    async def say_volumes_info(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptopia", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")

            embed.add_field(name="Base Volume :", value=self.get_base_volume(), inline=False)

            embed.add_field(name="Base Volume (sell) :", value=self.get_sell_base_volume(), inline=True)
            embed.add_field(name="Volume (sell) :", value=self.get_sell_volume(), inline=True)
            embed.add_field(name="Base Volume (buy):", value=self.get_buy_base_volume(), inline=True)
            embed.add_field(name="Volume (buy):", value=self.get_buy_volume(), inline=True)
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="cryptopia")
    async def say_prices_info(self):
        try:
            embed = discord.Embed(title="Ark(ARK) - Cryptopia prices info", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Open price :", value="{0} BTC".format(self.get_open_price(), inline=True))
            embed.add_field(name="Close price :", value="{0} BTC".format(self.get_close_price(), inline=True))

            embed.add_field(name="Low price :", value="{0} BTC".format(self.get_low_price(), inline=True))
            embed.add_field(name="High price :", value="{0} BTC".format(self.get_high_price(), inline=True))

            embed.add_field(name="Ask price :", value="{0} BTC".format(self.get_ask_price(), inline=False))
            embed.add_field(name="Last price :", value="{0} BTC".format(self.get_last_price(), inline=False))
            embed.add_field(name="Bid price :", value="{0} BTC".format(self.get_bid_price()))
            if float(self.get_change()) > 0.00:
                embed.add_field(name="Change :", value="{0} % :arrow_up:".format(self.get_change()))
            else:
                embed.add_field(name="Change :", value="{0} % :arrow_down:".format(self.get_change()))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")


def setup(bot):
    bot.add_cog(Cryptopia(bot))
