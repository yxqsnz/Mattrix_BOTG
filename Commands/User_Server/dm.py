import discord
from discord.ext import commands
@commands.command()
async def dm(ctx,Member:discord.Member=None,*,Mensagem="**Leave me Alone**"):
    if Member == None:
       await ctx.author.send("Uso: dm @usuário message")
       return
    try:
        await Member.send(Mensagem)
    except discord.Forbidden:
        await ctx.send("Desculpe esse Usuário Tem a dm **Fechada** ")
def setup(bot):
    bot.add_command(dm)