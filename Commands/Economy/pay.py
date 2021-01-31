from Scripts.database import Economy
from discord import Embed,Member
from random import randint
from discord.ext import commands
@commands.command(brief="trabalhar",aliases=['pagar'])
async def pay(ctx,Membro:Member=None,*,money=None):
    if not money.isnumeric():
        await ctx.send('Você colocou um valor invalido!')
        return
    else:
        money = int(money)
    if Membro == None or money == None:
        await ctx.reply('uso `<prefixodobot>pay <@membro/iddomembro> <quantia>`')
        return
    e = Embed()
    e.title = "Aguarde..."
    e.description = "Processando solicitação..."
    m = await ctx.send(embed=e)
    if Economy.find_one({"user_id":ctx.author.id}) == None:
      e.description = 'Você não tem uma conta!\ncrie uma conta usando `<prefixodobot>createprofile`'
      e.title = "Erro"
      await m.edit(embed=e)
    else:
        
        if Economy.find_one({"user_id":Membro.id}) == None:
            await ctx.reply(f"O {Membro} não tem conta!")
            return
        firstuser = Economy.find_one({"user_id":ctx.author.id})
        otheruser = Economy.find_one({"user_id":Membro.id})
        
     
        firstuser_money = int(firstuser['money'])
        otheruser_money = int(otheruser['money'])
        if firstuser_money < money:
            await ctx.reply('Você não tem Mattrix Money Suficiente!')
            return
        else:
            firstuser_money -= money
            otheruser_money += money
        Economy.update_one({'money': firstuser['money']},{'$set':{"money": firstuser_money}})
        Economy.update_one({'money': otheruser['money']},{'$set':{"money": otheruser_money}})
        e.title = "Ok!"
        e.description = f"o {ctx.author.mention} pagou para {Membro.mention} com o valor: {money}\n agora {ctx.author.mention} tem {firstuser_money} MM eo\n{Membro.mention} tem {otheruser_money} MM."

        await m.edit(embed=e)
def setup(bot):
    bot.add_command(pay)