from Scripts.database import Economy
from discord import Embed
from random import randint
from discord.ext import commands
@commands.command(brief="trabalhar",aliases=['trabalhar'])
async def work(ctx):
    e = Embed()
    e.title = "Aguarde..."
    e.description = "Processando solicitação..."
    m = await ctx.send(embed=e)
    if Economy.find_one({"user_id":ctx.author.id}) == None:
      e.description = 'Você não tem uma conta!\ncrie uma conta usando `<prefixodobot>createprofile`'
      e.title = "Erro"
      await m.edit(embed=e)
    else:
        i = Economy.find_one({"user_id":ctx.author.id})
        tog = randint(0,10)
        currentmoney=int(i['money'])
        newcurrentmoney = currentmoney + tog
        Economy.update_one({'money': currentmoney},{'$set':{"money": newcurrentmoney}})
        e.title = "Nice!"
        e.description = f"Você recebeu {tog} Mattrix Money!"

        await m.edit(embed=e)
def setup(bot):
    bot.add_command(work)