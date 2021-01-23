from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


@commands.command()
@has_permissions(manage_messages=True)
async def say(ctx, *,args):
        await ctx.send(args)
        await ctx.message.delete()
@say.error
async def say_error(error,ctx):
    if isinstance(error, CheckFailure):
        await ctx.reply("400| você Não tem perm de usar o comando `say`")
def setup(bot):
    
    bot.add_command(say)