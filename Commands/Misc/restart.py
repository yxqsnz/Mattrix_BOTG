#OK!?
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
import Scripts.BotMGR as MBM
import time
import discord,os
import signal,sys
from main import bot
@commands.command()

async def Restart(ctx):
    id = str(ctx.author.id)
  
    if id == '450812271451439124' or id == '567853754825572352':
      await MBM.RESTART_BOT(ctx,bot)
    else:
       print("Você Não Pode Executar Esse Comando.")

def setup(bot):
    bot.add_command(Restart)