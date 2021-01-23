import discord
import aiohttp
import main
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from main import bot

@commands.command()
async def testwh(ctx):
    pass
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discordapp.com/api/webhooks/799396597225750529/94d-ODA76vsT5MA8L3sWMj08a1RQ5l_QPpKF2AEQ-pAzOUTEpmpiETtOlHnbBZvwiAZg', adapter=AsyncWebhookAdapter(session))
        await webhook.send('Olá', username='hi!')

def setup(bot):
    bot.add_command(testwh)