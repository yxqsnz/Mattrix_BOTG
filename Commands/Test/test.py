from discord.ext import commands


@commands.command()
async def teste(ctx):
   await ctx.send("awman")
def setup(bot):
    
    bot.add_command(teste)