import discord
from discord.ext import commands
import sqlite3
import asyncio
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
cardinal = commands.Bot(command_prefix="SAO ")
crystaln = commands.Bot(command_prefix="NPCC ")
cardinal.remove_command('help')
crystaln.remove_command('help')
@cardinal.event
async def on_start():
    print("loaded")
@crystaln.event
async def on_start():
    print("loaded")
@cardinal.command()
async def test(ctx,user:discord.User):
    response = requests.get(user.avatar_url)
    img = Image.open(BytesIO(response.content), 'r')
    img=img.resize((144, 144))
    name=user.display_name
    font=ImageFont.truetype('msyh.ttc',28) #173 93
    background = Image.open('test.png', 'r')
    draw=ImageDraw.Draw(background)
    draw.text((180,93),name,font=font,fill="white")
    offset = (19,22)
    background.paste(img, offset)
    background.save('get.png')
    await ctx.send(file=discord.File('get.png'))
@test.error
async def test_on_error(ctx,error):
    error = str(error)
    if error == "user is a required argument that is missing.":
        response = requests.get(ctx.author.avatar_url)
        img = Image.open(BytesIO(response.content), 'r')
        img=img.resize((144, 144))
        name=ctx.author.display_name
        font=ImageFont.truetype('msyh.ttc',28) #173 93
        background = Image.open('test.png', 'r')
        draw=ImageDraw.Draw(background)
        draw.text((180,93),name,font=font,fill="white")
        offset = (19,22)
        background.paste(img, offset)
        background.save('get.png')
        await ctx.send(file=discord.File('get.png'))
    elif error.__contains__("User") and error.__contains__("not found"):
        await ctx.send("\❗此玩家不存在\❗")
try:
    loop = asyncio.get_event_loop()
    loop.create_task(cardinal.start("我才不告訴你勒"))
    loop.create_task(crystaln.start("我才不告訴你勒"))
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()
    quit()