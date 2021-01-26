from discord.ext import commands
import discord
from discord.ext.commands import MissingRequiredArgument
@commands.command(aliases=['mídia','midia'],brief="Mostra uma mídia")
async def atc(ctx,*,args=""):
   
    if args == "":
        await ctx.send("Erro você não botou nenhum link!")
        return
    if "@everyone" in args or "@here" in args:
       
        await ctx.send(":x:| everyone e here não são permitidos!!")
        return
    else:
        embed = discord.Embed(
            title="O:",
        )
        embed.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.name)
        embed.set_image(url=args)
        await ctx.send(embed=embed)
@atc.error
async def atc_error(e,ctx):
    if isinstance(e,MissingRequiredArgument):
        await ctx.reply("Erro você não botou nenhum link!")
def setup(bot):
    
    bot.add_command(atc)