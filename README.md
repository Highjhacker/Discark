# Discark

Ark Discord bot.

## Built with
- [Python](https://www.python.org/)
- [Discord.py](https://github.com/Rapptz/discord.py)
- [Requests](http://docs.python-requests.org/en/master/)
- [Arrow](http://arrow.readthedocs.io/en/latest/)
- [Gunicorn](http://gunicorn.org/)
- [Heroku](https://dashboard.heroku.com/)

## Current Features
- Can get the price from CoinMarketCap
- Can get the full informations from CoinMarketCap and output it in a human readable format
- Transform the timestamp to a human readable format with the Arrow library
- Display the current Ark price (in usd, from CoinMarketCap) in the bot status

## TODOS

- [ ] Unit testing
- [ ] Handle Markets
    - [ ] Binance
    - [x] Bittrex
    - [x] Cryptopia
        - [ ] Still some tweaks to do, but it works rn.
    - [x] COSS - No API currently
    - [x] Cryptomate
    - [x] LiteBit.eu
        - [ ] Some tweaks and fixes to do, not sure about the embed in the constructor
- [ ] Handle others site like CoinMarketCap
    - [x] Coinmarketcap
    - [ ] BraveNewCoin
    - [ ] CoinCodex
    - [x] CryptoCompare
    - [ ] CoinGecko
    - [ ] WorldCoinIndex
- [x] Allow the user to specify the fiat for the Ark Price (Yen, Euros, Dollars, ...)
- [ ] Better errors handling
- [ ] DRY
- [ ] Find a way to calculate the difference between two request for the Bittrex ticker and 
display  if the price is up or down
- [ ] PEP compliance
- [ ] Better commands syntax
- [ ] Try to regroup some fields inside the embed output
- [ ] ASYNC ASYNC ASYNC (replace requests with aiohttp if possible)
- [ ] Integrate Pythark
- ...

## Authors

- Jolan Beer - Highjhacker

## License

DiscArk is under MIT license. See the [LICENSE file](https://github.com/Highjhacker/Ark-Elixir/blob/master/LICENSE) for more informations.

