import discord,random
from discord.ext import commands
@commands.command(aliases=['8ball'])
async def eightball(ctx):
    a = ['Não','Sim','Pode ser','Num acredito que seja verdade','Mano?',"pode ser que sim ou pode ser que não"]
    await ctx.reply(random.choice(a))


def setup(bot):
    bot.add_command(eightball)