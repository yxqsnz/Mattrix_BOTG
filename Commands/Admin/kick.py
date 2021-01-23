import discord
from discord.ext  import commands
@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,Member:discord.Member=None):
    if Member == None:
        await ctx.reply('Uso: kick @Membro')
        return
    Member.kick()
    Member.send(f'Você foi expulso de {ctx.guild.name}!')
def setup(bot):
    bot.add_command(kick)