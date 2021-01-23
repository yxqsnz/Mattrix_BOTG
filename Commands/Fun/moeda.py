import random
from discord.ext import commands 
@commands.command()
async def moeda(ctx,arg=None):
    if arg == None:
        await ctx.send("Uso `moeda <cara/coroa>`")
        return
    pc = ['cara','coroa']
    sl = random.choice(pc)
    if arg == 'coroa' and sl == 'cara':
       await ctx.send('Eu ganhei!')
    elif sl == 'coroa' and arg == 'cara':
        await ctx.send('Você venceu!')
    else:
       await  ctx.send("EMPATE!")

def setup(bot):
    bot.add_command(moeda)