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
    - [ ] Bittrex
    - [ ] Cryptopia
    - [ ] COSS
    - [ ] Cryptomate
    - [ ] LiteBit.eu
- [ ] Handle others site like CoinMarketCap
    - [ ] BraveNewCoin
    - [ ] CoinMarketCap
    - [ ] CoinCodex
    - [ ] CryptoCompare
    - [ ] CoinGecko
    - [ ] WorldCoinIndex
- [ ] Allow the user to specify the fiat for the Ark Price (Yen, Euros, Dollars, ...)
- [ ] Better errors handling
- [ ] DRY
- [ ] Find a way to calculate the difference between two request for the Bittrex ticker and 
display  if the price is up or down
- [ ] PEP compliance
- [ ] Better commands syntax
- [ ] Try to regroup some fields inside the embed output
- ...

## Authors

- Jolan Beer - Highjhacker

## License

DiscArk is under MIT license. See the [LICENSE file](https://github.com/Highjhacker/Ark-Elixir/blob/master/LICENSE) for more informations.

