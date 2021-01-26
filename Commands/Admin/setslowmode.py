import discord
from discord.ext import commands
@commands.command(brief="Seta um delay no chat\nPrecisa da Permisão `Gerenciar mensagens`",description="Seta um Delay no chat")
@commands.has_permissions(manage_messages=True)
async def setslowmode(ctx,delay:str=None):
    if delay == None:
        await ctx.send('Uso: setslowmode <segundos>')
        return
    if not delay.isnumeric:
        await ctx.send("Somente **Numeros** são permitidos!")
        return
    await ctx.channel.edit(slowmode_delay=int(delay))
    pass
def setup(bot):
    bot.add_command(setslowmode)