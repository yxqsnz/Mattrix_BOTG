import discord
import aiohttp
from discord import embeds
import main
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from main import bot

@commands.command()
async def ytsearch(ctx,*,args=''):
    if not args:
        await ctx.send("Uso: `ytsearch <algumacoisa>`")
    link = ''
    link = str(args).replace('+',"%2B")
    args = link.replace(" ",'+')
    link = f"https://www.youtube.com/results?search_query={args}"
    embedVar = discord.Embed(title="Clique Aqui!",
     description="Pronto!",
     color=0xff0000,
     url=link,
     
     )
    embedVar.set_footer(text="Powered By Mattrix BOT")

    await ctx.send(embed=embedVar)
    #https://www.youtube.com/results?search_query=c%2B%2B
    pass

def setup(bot):
    bot.add_command(ytsearch)