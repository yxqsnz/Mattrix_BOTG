import discord
import aiohttp
import main
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from main import returncmds
@commands.command()
async def help(ctx):
    pass
    await ctx.send("Loading Help Commmand....")
    helpmsg = f"```fix\nBem vindo ao HELP COMMAND!\nEsses são os meus comandos!\n{str(returncmds())} ```"
    await ctx.send(helpmsg)
def setup(bot):
    bot.remove_command('help')
    bot.add_command(help)