from discord import embeds
from prawcore.exceptions import Redirect
from Scripts.RedditController import reddit
import discord,random
from random import choice, randint
from discord.ext import commands
@commands.command(brief="Pega um Meme no Reddit",description="Pega Um meme no reddit [anime/SubReddit]")

async def rmeme(ctx,subreddit=None):
    memessb = ['famil','memes','wholesomememes']
    animesubr = ['animememes','Animemes']
    sl = ""
    if subreddit == None:
        sl = random.choice(memessb)
    elif subreddit == 'anime':
        sl = random.choice(animesubr)
    else:
        sl = subreddit
    tembed = discord.Embed(
        title='rmeme',
        description="Escolhendo um meme no Reddit....."
    )
    m = await ctx.send(embed=tembed)
    sub =""
    i  = randint(0,200)
    subreddit = reddit.subreddit(sl)
    sub =  reddit.subreddit(sl).random()
    
    if sub.over_18:
        if ctx.channel.is_nsfw():
           await ctx.send(":unlock: Aviso Esse conteudo é NSFW!")
        else:
            embedd = discord.Embed(
                title="Bloqueado!",
                description=":lock: Desculpe Como esse conteudo é NSFW!,e o Canal não tem O NSFW ativo eu não posso enviar esse conteudo!",
                color=0xff0000
            )
            await m.edit(embed=embedd)
            return
    embed = discord.Embed(
        title=sub.title,
        color=0xFFA500
    )
    embed.set_thumbnail(url=subreddit.icon_img)
    embed.set_footer(text=f'Meme em /r/{sl}')
    embed.set_author(name=sub.author.name,icon_url=sub.author.icon_img)
    embed.set_image(url=sub.url)
    await m.edit(embed=embed)
    
def setup(bot):
    bot.add_command(rmeme)