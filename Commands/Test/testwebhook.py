import requests
import discord,Scripts.envcontroller as env
from requests.api import head
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter
@commands.command()
async def testwhi(ctx):
    url = "https://discord.com/api/webhooks/803262794665164910/GnkUUGJyqwc-cOhvHFxDCn6W4TgfqsioEwtZCH-WvxxsLD2sAUGXJG6jaEvYXqSuEUxS"
    urlid = "https://discord.com/api/webhooks/803262794665164910"
    rpdata = {
        "channel_id":ctx.channel.id,
        "guild_id":ctx.guild.id
    }
    headers = {
         "Authorization": f"Bot {env.ReturnEnv('TOKEN')}" 
    }
    r = requests.patch(url,json=rpdata)

    await ctx.send(r.status_code)
    data = {
        "content":"Awman!"
    }
    await ctx.send(f"{r.status_code} {r.json} {r.content}")
    rr = requests.post(url,json=r.json())
def setup(bot):
    bot.add_command(testwhi)