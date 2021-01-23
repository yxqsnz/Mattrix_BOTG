import discord
from discord.ext import commands
@commands.command()
@commands.has_permissions(administrator=True)
async def setslowmode(ctx,arg:str=None):
    if arg == None:
        await ctx.send('Uso: setslowmode <segundos>')
        return
    if not arg.isnumeric:
        await ctx.send("Somente **Numeros** são permitidos!")
        return
    await ctx.channel.edit(slowmode_delay=int(arg))
    pass
def setup(bot):
    bot.add_command(setslowmode)