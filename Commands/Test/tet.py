from discord import Embed
import datetime
from discord.ext import commands
@commands.command()
async def tet(ctx):
    e:Embed = Embed(
        title="teste!"

    )
    e.set_footer(text="roi guys")
    e.timestamp = datetime.datetime.utcnow()
    e.description = "adnaiwhdaiwdbaiwdhbaiwudhaniwudh"
    await ctx.send(embed=e)
def setup(bot):
    bot.add_command(tet)