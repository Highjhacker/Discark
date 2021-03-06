import discord
import requests
from discord.ext import commands
import arrow
import json


class CoinMarketCap:
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://api.coinmarketcap.com/v1/ticker/"

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)

    def get_price(self):
        r = self.get("ark/")
        price = r.json()[0]["price_usd"]
        return price

    def get_price_bis(self, fiat=""):
        fiats = {
            "usd": u"\u0024",    # $ dollars
            "eur": u"\u20AC",    # euros
            "aud": u"\u0024",    # $ Australian
            "gbp": u"\u00A3",    # livres
            "jpy": u"\u00A5",    # Yen
            "brl": u"R\u0024",   # Brazil real
            "cad": u"\u0024",    # $ Canada
            "chf": u"CHF",       # Franc suisse
            "clp": u"\u0024",    # Peso chilien
            "cny": u"\u00A5",    # Yuan chinois
            "czk": "CZK",        # couronnes tchèques
            "dkk": "DKK",        # couronnes danoise
            "hkd": u"HK\u0024",  # Hong Kong $
            "huf": "HUF",        # Florins hongrois
            "idr": "Rp",         # Roupie indonésienne
            "ils": u"\u20AA",    # Shekel israélien
            "inr": u"\u20B9",    # Rupee indienne
            "krw": u"\u20A9",    # Won sud coréen
            "mxn": u"\u0024",    # Peso mexicain
            "myr": "MYR",        # Ringgit malais
            "nok": "NOK",        # Couronne norvégienne
            "nzd": "NZD",        # $ Néo zélandais
            "php": u"\u20B1",    # Peso philipin
            "pkr": u"\u20A8",    # Pakistan rupee
            "pln": u"\u007A\u0142",     # Polish zloti
            "rub": u"\u20BD",     # Russian ruble
            "sek": "SEK",         # Couronne suédoise
            "sgd": u"S\u0024",    # Singapour $
            "thb": u"\u0E3F",     # Bat thailande
            "try": u"\u20BA",     # Turkish lyra
            "twd": u"NT\u0024",   # Taiwan $
            "zar": "ZAR"          # Rand sud africain
        }
        if fiat:
            if fiat in fiats:
                r = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/ark/?convert=%s" % fiat).text)
                price = r[0]["price_%s" % fiat][0:7]
                return price + " {0}".format(fiats[fiat])
        else:
            r = self.get("ark/")
            price = r.json()[0]["price_usd"]
            return price + " $"

    def get_volume_usd(self):
        r = self.get("ark/")
        volume = r.json()[0]["24h_volume_usd"]
        return volume

    def get_available_supply(self):
        r = self.get("ark/")
        available_supply = r.json()[0]["available_supply"]
        return available_supply

    def get_id(self):
        r = self.get("ark/")
        id = r.json()[0]["id"]
        return id

    def get_last_updated(self):
        r = self.get("ark/")
        last_updated = r.json()[0]["last_updated"]
        return arrow.Arrow.fromtimestamp(last_updated).humanize()

    def get_market_cap(self):
        r = self.get("ark/")
        market_cap = r.json()[0]["market_cap_usd"]
        return market_cap

    def get_max_supply(self):
        r = self.get("ark/")
        max_supply = r.json()[0]["max_supply"]
        return max_supply

    def get_name(self):
        r = self.get("ark/")
        name = r.json()[0]["name"]
        return name

    def get_percent_change_one_hour(self):
        r = self.get("ark/")
        price = r.json()[0]["percent_change_1h"]
        return price

    def get_percent_change_day(self):
        r = self.get("ark/")
        price = r.json()[0]["percent_change_24h"]
        return price

    def get_percent_change_week(self):
        r = self.get("ark/")
        price = r.json()[0]["percent_change_7d"]
        return price

    def get_price_btc(self):
        r = self.get("ark/")
        price = r.json()[0]["price_btc"]
        return price

    def get_rank(self):
        r = self.get("ark/")
        rank = r.json()[0]["rank"]
        return rank

    def get_symbol(self):
        r = self.get("ark/")
        symbol = r.json()[0]["symbol"]
        return symbol

    def get_total_supply(self):
        r = self.get("ark/")
        total_supply = r.json()[0]["total_supply"]
        return total_supply

    @commands.command(name="info")
    async def say_infos(self):
        try:
            embed = discord.Embed(title="{0}({1}) - CoinMarketCap".format(self.get_name(), self.get_symbol()), colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")

            #embed.add_field(name="Name", value=self.get_name(), inline=True)
            #embed.add_field(name="Symbol", value=self.get_symbol(), inline=True)
            #embed.add_field(name="ID", value=self.get_id(), inline=True)
            embed.add_field(name="Rank", value=self.get_rank(), inline=False)

            embed.add_field(name="Price", value=self.get_price() + " $", inline=True)
            embed.add_field(name="Price (BTC)", value=self.get_price_btc() + " BTC", inline=True)

            embed.add_field(name="Volume (24h)", value=self.get_volume_usd() + " $", inline=False)
            embed.add_field(name="Market Cap", value=self.get_market_cap() + " $", inline=False)

            embed.add_field(name="Circulating supply", value=self.get_available_supply() + " Ѧ", inline=False)
            #embed.add_field(name="Max supply", value=self.get_max_supply(), inline=False)
            embed.add_field(name="Total supply", value=self.get_total_supply() + " Ѧ", inline=False)

            if float(self.get_percent_change_one_hour()) > 0.00:
                embed.add_field(name="% change (1h)", value=self.get_percent_change_one_hour() + " % :arrow_up:", inline=False)
            else:
                embed.add_field(name="% change (1h)", value=self.get_percent_change_one_hour() + " % :arrow_down:", inline=False)

            if float(self.get_percent_change_day()) > 0.00:
                embed.add_field(name="% change (24h)", value=self.get_percent_change_day() + " % :arrow_up:", inline=False)
            else:
                embed.add_field(name="% change (24h)", value=self.get_percent_change_day() + " % :arrow_down:", inline=False)

            if float(self.get_percent_change_week()) > 0.00:
                embed.add_field(name="% change (7days)", value=self.get_percent_change_week() + " % :arrow_up:", inline=False)
            else:
                embed.add_field(name="% change (7days)", value=self.get_percent_change_week() + " % :arrow_down:", inline=False)

            embed.add_field(name="Last update", value=self.get_last_updated(), inline=False)

            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")

    @commands.command(name="price")
    async def say_price(self, fiat=""):
        try:
            embed = discord.Embed(title="Ark(ARK) - CoinMarketCap", colour=discord.Colour.dark_red())
            embed.set_thumbnail(url="https://ark.io/images/mediakit/Red-Toxic.png")
            embed.add_field(name="Current price :", value=self.get_price_bis(fiat))
            await self.bot.say(embed=embed)
        except commands.CommandError as e:
            await self.bot.say("Command invalid.")


def setup(bot):
    bot.add_cog(CoinMarketCap(bot))