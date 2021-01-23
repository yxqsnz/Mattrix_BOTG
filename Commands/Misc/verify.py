import discord
import aiohttp
import main
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from main import bot

@commands.command()
async def verify(ctx,arg1="",arg2=""):
    pass
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/800104328018001970/JstaHWMmc9sFZhQjfXEntetdfiPHOnwxyMsG_uEDdP5KyHGR4A2y8YY9y8oNivRYbOm6', adapter=AsyncWebhookAdapter(session))
        if (arg1):
         pass
        else:
            await webhook.send(
                'Olá,uso: `m!verify gen` para gerar um hash de verificação, `m!verify verify <seuhash>` para verificar a sua conta quando for reiniciar o bot.',
                username='Verify!')


def setup(bot):
    bot.add_command(verify)