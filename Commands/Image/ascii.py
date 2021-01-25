from os import wait
import pyfiglet

from discord.ext import commands
@commands.command()
async def ascii(ctx,*,args=None):
    if args == None:
        await ctx.send("Uso: ascii <texto>")
        return
    if len(args) > 40:
        await ctx.send("O texto é muito Grande!")
        return
    r = pyfiglet.figlet_format(args,font = "slant")
    await ctx.send(f"```{r}``` ")
def setup(bot):
    bot.add_command(ascii)