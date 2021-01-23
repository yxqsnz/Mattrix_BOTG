from random import randint, random
from Scripts.RedditController import reddit
import discord
from discord.ext import commands

@commands.command()
async def testr(ctx):
    tembed = discord.Embed(
        title='Aguarde',
        description="Escolhendo um meme no reddit....."
    )
    m = await ctx.send(embed=tembed)
    a =""
    i  =randint(0,200)
    for submission in reddit.subreddit("memes").hot(limit=i):
      a = submission
    embed = discord.Embed(
        title=a.title,
    )
    embed.set_author(name=a.author.name)
    embed.set_image(url=a.url)
    await m.edit(embed=embed)
def setup(bot):
    bot.add_command(testr)