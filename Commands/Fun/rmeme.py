from discord import embeds
from prawcore.exceptions import Redirect
from Scripts.RedditController import reddit
import discord
from random import choice, randint
from discord.ext import commands
@commands.command()

async def rmeme(ctx,arg=None):
    memessb = ['famil','memes','wholesomememes']
    animesubr = ['animememes','Animemes']
    if arg == None:
        arg = choice(memessb)
    if arg == 'anime':
        arg = choice(animesubr)
    tembed = discord.Embed(
        title='rmeme',
        description="Escolhendo um meme no reddit....."
    )
    m = await ctx.send(embed=tembed)
    sub =""
    i  = randint(0,200)
    subreddit = reddit.subreddit(arg)
    sub =  reddit.subreddit(arg).random()
    embed = discord.Embed(
        title=sub.title,
        color=0xFFA500
    )
    embed.set_thumbnail(url=subreddit.icon_img)
    embed.set_footer(text=f'meme em /r/{arg}')
    embed.set_author(name=sub.author.name,icon_url=sub.author.icon_img)
    embed.set_image(url=sub.url)
    await m.edit(embed=embed)
def setup(bot):
    bot.add_command(rmeme)