
from discord.ext import commands
import discord,random
from discord.ext.commands.errors import MissingPermissions
bangifs =['https://tenor.com/view/banido-gif-18007190','https://tenor.com/view/banido-will-smith-will-smith-banido-tayklor-bibi-viado-gif-16569411','https://tenor.com/view/will-smith-banido-meme-dance-gif-16971203']
@commands.command(brief="Bane um Membro\nPrecisa da Permisão `Banir Membros`")
@commands.has_permissions(ban_members=True)
async def ban(ctx,Member:discord.Member=None,*,args=None):
    if ctx.author == Member:
        await ctx.reply("Você não pode se-banir!")
        return
    if Member == None:
        await ctx.send('Uso: ban @Membro <Motivo>')
        return
    if args == None:
        args == "**Motivo Não especificado.**"
    try:
        await Member.ban(reason=args)
    except MissingPermissions:
        await ctx.send(f"Eu não tenho perm para Banir {Member.mention} ")
    try:
        await Member.send(f"Você foi BANIDO do servidor {ctx.guild.name} Por {args}.")
    except:
        pass
    pass
    await ctx.channel.send(f"{Member.display_name} Foi Banido por {ctx.author.name}!")
    await ctx.channel.send(random.choice(bangifs))
def setup(bot):
    
    bot.add_command(ban)