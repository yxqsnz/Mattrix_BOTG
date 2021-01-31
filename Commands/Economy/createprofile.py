from Scripts.database import Economy
from discord import Embed
from discord.ext import commands
@commands.command(brief="Criar uma conta para o bot!",aliases=['criarconta','createprofile'])
async def cprofile(ctx):
    e = Embed()
    e.title = "Criando seu perfil..."
    e.description = "Processando solicitação..."
    e.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    m = await ctx.send(embed=e)
    data = {
        "user_id": ctx.author.id,
        "money":0,
        "job":"Padrão"
    }
    if Economy.find_one({"user_id":ctx.author.id}) == None:
        Economy.insert_one(data)
        e.title = "Perfil criado!"
        e.description = "pronto!"
        await m.edit(embed=e)
    else:
        e.title = "Erro"
        e.description = "Você já tem uma conta!"
        await m.edit(embed=e)
def setup(bot):
    bot.add_command(cprofile)