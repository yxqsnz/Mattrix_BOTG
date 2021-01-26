import discord
from discord.ext import commands
@commands.command(brief="...",description="...")
async def kill(ctx,Member:discord.Member=None):
    if Member == None:
        Member = ctx.author
    await ctx.send(f"{ctx.author.mention} Matou {Member.mention}")
def setup(bot):
    bot.add_command(kill)