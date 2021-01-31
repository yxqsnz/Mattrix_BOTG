import discord
from discord.ext import commands
from main import bot
@commands.command()
async def dm(ctx,Member:discord.Member=None,*,Mensagem="**Leave me Alone**"):
	
	e = 803585399774511135
	paperplane = bot.get_emoji(id=e)
	if Member == None:
		await ctx.send("Uso: dm @usuário message")
		return
	try:
		await Member.send(Mensagem)
		await ctx.message.add_reaction(paperplane)
	except discord.Forbidden:
		await ctx.send("Desculpe esse Usuário Tem a dm **Fechada** ")
def setup(bot):
    bot.add_command(dm)