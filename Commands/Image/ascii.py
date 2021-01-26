from os import wait
import pyfiglet

from discord.ext import commands
@commands.command(brief="Transforma um texto para ascii art")
async def ascii(ctx,*,texto=None):
    if texto == None:
        await ctx.send("Uso: ascii <texto>")
        return
    if len(texto) > 40:
        await ctx.send("O texto é muito Grande!")
        return
    r = pyfiglet.figlet_format(texto,font = "slant")
    await ctx.send(f"```{r}``` ")
def setup(bot):
    bot.add_command(ascii)
    