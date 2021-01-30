from redbot.core import commands

class PokeBattle(commands.Cog):
    """Poke Battle"""

    @commands.command()
    async def pokebattle(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
