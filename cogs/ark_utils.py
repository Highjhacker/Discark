from discord.ext import commands


class ArkUtils:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="whitepaper")
    async def get_whitepaper(self):
        await self.bot.say("https://ark.io/Whitepaper.pdf")

    @commands.command(name="roadmap")
    async def get_roadmap(self):
        await self.bot.say("https://ark.io/roadmap")

    @commands.command(name="ark")
    async def get_official_website(self):
        await self.bot.say("https://ark.io/")

    @commands.command(name="ledger")
    async def get_ledger_tuto(self):
        await self.bot.say("https://blog.ark.io/full-ledger-nano-s-hardware-wallet-guide-for-ark-7bf7bfff4cef")

    @commands.command(name="reddit")
    async def get_subreddit(self):
        await self.bot.say("https://www.reddit.com/r/ArkEcosystem")

    @commands.command(name="51")
    async def get_delegates_stats(self):
        await self.bot.say("https://www.arknode.net/VoteReport.txt")

    @commands.command(name="delmonitor")
    async def get_delegate_monitor(self):
        await self.bot.say("https://explorer.ark.io/delegateMonitor")

    @commands.command(name="stats")
    async def get_ark_stats(self):
        await self.bot.say("https://arkstats.net/")

    @commands.command(name="calc")
    async def calculator(self, delegate_name=""):
        #A modifier impérativement parce que c'est le foutoir, mais c'était histoire de vite faire et d'avoir un prototype
        #fonctionnel.
        delegates_list = {
            "jarunik": "https://docs.google.com/spreadsheets/d/1QawUqYa_e9YN_3Stb3-WYTdJ2BgnYqxsErYbA2ihXjo/edit?usp=sharing",
            "dafty": "https://docs.google.com/spreadsheets/d/1FGo3FkC3uSWXGHatPQyny2brMWjAIJsHFCR-Lhkl_m0/edit?usp=sharing",
            "toons": "https://docs.google.com/spreadsheets/d/1FGo3FkC3uSWXGHatPQyny2brMWjAIJsHFCR-Lhkl_m0/edit?usp=sharing",
            "reconnico": "http://calculator.reconnico.com/",
            "faustbrian": "https://delegates.arkx.io/calculator",
            "bioly": "http://pool.arkno.de/calculator.php"
        }
        delegate_name = delegate_name.lower()
        if delegate_name:
            if delegate_name in delegates_list:
                await self.bot.say(delegates_list[delegate_name])
            else:
                await self.bot.say("Invalid delegate's name. The valids names are : jarunik, dafty, toons, reconnico, faustbrian, bioly")
        else:
            await self.bot.say("Jarunik : <https://docs.google.com/spreadsheets/d/1QawUqYa_e9YN_3Stb3-WYTdJ2BgnYqxsErYbA2ihXjo/edit?usp=sharing>\n"
                               "Dafty : <https://docs.google.com/spreadsheets/d/1FGo3FkC3uSWXGHatPQyny2brMWjAIJsHFCR-Lhkl_m0/edit?usp=sharing>\n"
                               "Toons : <https://docs.google.com/spreadsheets/d/1dmFKza6cM3DYaNbKLlZg2rx6rZL5iLcYRLK5eEXXqD8/edit#gid=0>\n"
                               "Reconnico : <http://calculator.reconnico.com/>\n"
                               "Faustbrian : <https://delegates.arkx.io/calculator>\n"
                               "Bioly : <http://pool.arkno.de/calculator.php>\n")


def setup(bot):
    bot.add_cog(ArkUtils(bot))