from redbot.core import commands

class Trainer:
    def __init__(self, cog, member, team):
        self.team = team
        self.member = member
        self.bot = bot

class PokeBattle(commands.Cog):
    """Poke Battle"""

    @commands.command()
    async def pokebattle(self, bot, ctx):
        """This does stuff!"""
        player = Trainer(Self, ctx.member, [pikachu, totodile, abra] )
        await ctx.send(f"Name:{payer.member}. Bot:{payer.bot} Team:{payer.team}")
