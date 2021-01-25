import requests
from discord import Webhook, RequestsWebhookAdapter, webhook
from discord.ext import commands
from googletrans import Translator
import Scripts.envcontroller as env
import Scripts.wbapi as WebHookApiD
t = Translator()
uneux = WebHookApiD.Client()
uneux.Login(env.ReturnEnv("Uneux_webhook_url"))
uneux.SetAvatar("https://img2.gratispng.com/20180617/oek/kisspng-google-translate-translation-mobile-phones-android-google-translator-toolkit-5b2659dfc5b4e8.0868407315292400318098.jpg")
uneux.SetUsername("Mattrix Bot Translate  Powered by google translate!")

@commands.command(aliases=['tdz','translate'])

async def traduzir(ctx,arg=None,*,args=None):
    if arg == None:
        await ctx.send("USO: traduzir/translate/tdz <lang> hi")
        arg = "pt"
        return
    if args == None:
        await ctx.send("Coloque um texto para traduzir!")
        return
    tdz = t.translate(f"{args}", dest=arg)    
    if str(ctx.guild.id) == "693164410205765684":
        uneux.Send(f"De {tdz.src} Para {tdz.dest}: `{tdz.text}`")
        return
    await ctx.send(f"De {str(tdz.src).capitalize()} Para {str(tdz.dest).capitalize()}: `{tdz.text}`")
    del arg,args
def setup(bot):
    bot.add_command(traduzir)
    