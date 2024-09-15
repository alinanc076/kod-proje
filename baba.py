import random
import discord
from discord.ext import commands

import keraspy

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def resim (ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            await i.save(f"./images/{i.filename}")
            await ctx.send(f"{i.filename} resmini kaydettim")
            sinif,skor=keraspy.x(f"./images/{i.filename}")
            if sinif =="Guvercin\n":
                await ctx.send("Güvercin Bulgur ve Pirinç Yerler")
            elif sinif =="Serce\n":
                await ctx.send("Serçeler tohum, Böcek, meyve ve lavra yerler")
            elif sinif =="Karga\n":
                await ctx.send("Hemen hemen her şeyi yerler")
            elif sinif =="Diger\n":
                await ctx.send("Yer yada yemez")
            else:
                await ctx.send("Bir hata oldu")
    else:
        await ctx.send("Resim bulunamadı")

@bot.command()
async def muzik(ctx,tür):
    Şarkılar= {'rap': ["Cıstak","Yerli Plaka","Neyim Varki"],
               "pop":["Kuzu Kuzu","Aşkın Olayım","Beni Sev"],
               "metal":["Cano","Rastgele","Kafa Leyla","Patlat"]}
    if tür in Şarkılar.keys():
        x=random.choice (Şarkılar[tür])
        await ctx.send(x)
    else:
        await ctx.send("Bizde Şarkı Bulunmamakta, Başka Bul !!!")
    def ebob(a, b):
        while b: a, b = b, a % b
        return a

    def ekok(a, b):
        return abs(a * b) // ebob(a, b)

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'Bot hazır: {bot.user}')

    @bot.command()
    async def hesapla(ctx, a: int, b: int):
        await ctx.send(f"EBOB: {ebob(a, b)}\nEKOK: {ekok(a, b)}")
bot.run("TOKEN")