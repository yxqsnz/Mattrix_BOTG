import time
import discord,os,signal
from main import bot,rtk
async def RESTART_BOT(ctx,bot):
        await ctx.send("Reinciando...")
        print(f'[BOT.MANAGER/RESTART] REINICIANDO BOT...... POR {ctx.author} id:{ctx.author.id}')
        await bot.change_presence(
            activity=discord.Game(name="Reiniciando...."),
            status=discord.Status.dnd)
        time.sleep(5)
        await bot.close()
        os.system('exec python main.py')
       
        signal.alarm(1)
        await bot.change_presence(
            activity=discord.Game(name="Reiniciando...."),
            status=discord.Status.dnd)