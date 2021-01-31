from Scripts.database import Economy
from discord import Embed,Member
from discord.ext import commands
@commands.command(brief="hmmm",aliases=['money'])
async def profileinfo(ctx,Membro:Member=None):
    if Membro == None:
           Membro = ctx.author
    e = Embed()
    e.title = "Aguarde..."
    e.description = "Processando solicitação..."
    m = await ctx.send(embed=e)
    if Economy.find_one({"user_id":Membro.id}) == None:
      e.description = f'{Membro.mention} não tem uma conta!\ncrie uma conta usando `<prefixodobot>createprofile`'
      e.title = "Erro" 
      await m.edit(embed=e)
    else:
        i = Economy.find_one({"user_id":Membro.id})
        e.title = "Pronto!"
        e.description = f"perfil de {Membro.mention}"
        e.add_field(name="Money (MM)",value=str(i['money']),inline=False)
        e.add_field(name="Emprego",value=str(i['job']),inline=False)
        await m.edit(embed=e)
def setup(bot):
    bot.add_command(profileinfo)