import discord
from discord.ext import commands
@commands.command()
async def dm(ctx,Member:discord.Member=None,*,args="**Leave me Alone**"):
    if Member == None:
       await ctx.author.send("Uso: dm @usuario message")
       return
    try:
        await Member.send(args)
    except discord.Forbidden:
        await ctx.send("Desculpe esse Usuario Tem a dm **Fechada** ")
def setup(bot):
    bot.add_command(dm)