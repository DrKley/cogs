from .pokebattle import PokeBattle


async def setup(bot):
    cog = PokeBattle(bot)
    bot.add_cog(cog)