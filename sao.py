import base
import sqlite3
import discord
from discord.ext import commands
import asyncio
import random
from PIL import Image, ImageFont, ImageDraw
cardinal = commands.Bot(command_prefix="SAO ")
crystaln = commands.Bot(command_prefix="NPCC ")
cardinal.remove_command('help')
painAbsorber = 10
@cardinal.command()
async def say(ctx, arg):
    if ctx.author.id == "611418694245154847":
        await ctx.send(arg)
@cardinal.command(name="LINK")
async def _LINK_START(ctx, a:str): #驗證
    cv=cardinal.get_channel(733301367682105346)
    lifeB=cardinal.get_channel(733655240749875251)
    if ctx.channel == cv:
        if a == "START!":
            db=sqlite3.connect('user.sqlite')
            cursor=db.cursor()
            cursor.execute(f"SELECT user_id FROM user WHERE user_id = {ctx.author.id}")
            c = cursor.fetchall()
            await ctx.send(file=discord.File('linkstart!.mp4'))
            if c == []:
                sql = ("INSERT INTO user(user_id, username, hp, atk, accy, def, position, item, exp, level, guild, isGuildMaster,marryname, marryid, money, hplimit, killc,wpn) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
                val = (str(ctx.author.id), str(ctx.author.display_name), 1000, random.randrange(30, 40), random.randrange(50, 100), random.randrange(10, 20), "起始之鎮", "",0, 0, None,0, None, None, 100, 1000, 0,"拳頭")
                cursor.execute(sql, val)
                db.commit()            
            await asyncio.sleep(10)
            user = ctx.message.author
            role = discord.utils.get(ctx.guild.roles, name="存活")
            await user.add_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="綠名")
            await user.add_roles(role)
    else: 
        await ctx.send("還想抓bug啊")
@cardinal.command()
async def go(ctx):
    await ctx.send("待寫完")
@cardinal.command()
async def test(ctx):
    await ctx.send('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\na')
@cardinal.command()
async def createGuild(ctx, arg):
    bugReport=cardinal.get_channel(733659457849917531)
    guild=base.guild(ctx.author.id)
    if guild == None:
        try:
            db=sqlite3.connect('user.sqlite')
            cursor=db.cursor()
            colour=discord.Color(random.randint(0, 0xFFFFFF))
            author = ctx.message.author
            guild = ctx.guild
            await guild.create_role(name=arg, hoist=True, color=colour)
            role = discord.utils.get(ctx.guild.roles, name=arg)
            user = ctx.message.author
            await user.add_roles(role)
            cursor.execute(f"UPDATE user SET guild=?,isGuildMaster=? WHERE user_id=?", (arg, 1 ,str(ctx.author.id)))
            db.commit()
            await ctx.send(f"創建公會:{arg} 成功")
        except Exception as e:
            await bugReport.send(f"ERRORCODE:{e}")
    else:
        await ctx.send("雖然是公會 但可不是鬧著創的")
@cardinal.command()
async def joinGuild(ctx, arg):
    bugReport=cardinal.get_channel(733659457849917531)
    guild=base.guild(ctx.author.id)
    if guild == None:
        try:
            db=sqlite3.connect('user.sqlite')
            cursor=db.cursor()
            cursor.execute(f"UPDATE user SET guild=?,isGuildMaster=? WHERE user_id=?", (arg, 0,str(ctx.author.id)))
            guild = ctx.guild
            role = discord.utils.get(ctx.guild.roles, name=arg)
            user = ctx.message.author
            await user.add_roles(role)
            db.commit()
            await ctx.send(f"成功加入公會: {arg}")
        except AttributeError:
            await ctx.send("公會不存在,若要繼續加入公會請再次輸入指令")
        else:
            await bugReport.send(f"ERROR CODE:{Exception}")
    else:
        await ctx.send("雖然是公會 但可不是鬧著進的")
@cardinal.command()
async def allGuildOwner(ctx):
    db=sqlite3.connect('user.sqlite')
    cursor=db.cursor()
    cursor.execute("SELECT guild FROM user WHERE isGuildMaster=1")
    ago=cursor.fetchall()
    cursor.execute("SELECT username FROM user WHERE isGuildMaster=1")
    ugo=cursor.fetchall()
    col=0
    get=None
    for f in ago:
        cursor.execute("SELECT guild FROM user WHERE isGuildMaster=1")
        ago1=cursor.fetchall()[col][0]
        cursor.execute("SELECT username FROM user WHERE isGuildMaster=1")
        ugo1=cursor.fetchall()[col][0]
        if get != None:
            get=f"{get}{ago1}\t{ugo1}\n"
        else:
            get=f"{ago1}\t{ugo1}\n"
        col+=1
    await ctx.send(get)
@cardinal.command()
async def leaveGuild(ctx):
    owner=base.guildOwner(ctx.author.id)
    guild=base.guild(ctx.author.id)
    await ctx.message.author.remove_roles(guild)
@cardinal.command()
async def marry(ctx, user:discord.User):
    if user.id != ctx.author.id:
        db=sqlite3.connect('user.sqlite')
        cursor=db.cursor()
        cursor.execute(f"SELECT marryname FROM user WHERE user_id={ctx.author.id}")
        c = cursor.fetchall()
        cursor.execute(f"SELECT marryname FROM user WHERE user_id={user.id}")
        d = cursor.fetchall()
        skip = False
        if c == [(None,)] and d == [(None,)]:
            await ctx.send(f"{user.mention}, 你願意嫁給 {ctx.author.mention} 嗎?\n願意請按<:yes:737278559651102811> 不願意請按<:no:737278338774859816> (不按會在60秒後取消)")
            def confirm(reaction, user):
                return user == user and str(reaction.emoji) == '<:yes:737278559651102811>' or str(reaction.emoji) == '<:no:737278338774859816>'
            try:
                reaction, user = await cardinal.wait_for('reaction_add', timeout=60.0, check=confirm)
            except asyncio.TimeoutError:
                await ctx.send('時限過了,也許他不想跟你結婚,別哭')
                skip = True
            if str(reaction.emoji) == '<:yes:737278559651102811>' and skip != True:
                await ctx.send('成功結婚')
                cursor.execute(f"UPDATE user SET marryname=?, marryid=? WHERE user_id=?",(user.display_name, user.id, ctx.author.id))
                cursor.execute(f"UPDATE user SET marryname=?, marryid=? WHERE user_id=?",(ctx.author.display_name, ctx.author.id, user.id))
                db.commit()
            elif str(reaction.emoji) == '<:no:737278338774859816>' and skip != True:
                await ctx.send("別哭...這只是個遊戲,別太認真")
        elif c == [(None,)] and d != [(None,)]:
            d = str(d[0][0])
            await ctx.send(f"他已經與:{d}  結婚了")
        elif c != [(None,)] and d == [(None,)]:
            c = str(c[0][0])
            await ctx.send(f"你已經與:{c}  結婚了")
        elif c != [(None,)] and d != [(None,)] and c==d:
            await ctx.send("你們結婚了")
        else:
            await ctx.send("你們?")
    else:
        await ctx.send("難道你想跟自己結婚嗎????")
@cardinal.command()
async def duel(ctx,user: discord.User):
    db=sqlite3.connect('user.sqlite')
    c=db.cursor()
    c.execute("UPDATE user SET duel=? WHERE user_id=?",(0,ctx.author.id))
    db.commit()
@cardinal.command()
async def attack(ctx, arg, user: discord.User):
    userr=ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="黃名")
    await userr.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name='綠名')
    await userr.remove_roles(role)
    db=sqlite3.connect('user.sqlite')
    c=db.cursor()
    wpn=base.wpn(ctx.author.id)
    ctxhp=base.hp(ctx.author.id)
    auhp=base.hp(user.id)
    ctxatk=random.randint(base.atk(ctx.author.id)+base.wpnatk(ctx.author.id)-20,base.atk(ctx.author.id)+base.wpnatk(ctx.author.id)+20)
    ctxdef=random.randint(base.def_(ctx.author.id)-15,base.def_(ctx.author.id)+15)
    audef=random.randint(base.def_(user.id)-15,base.def_(user.id)+15)
    ctxaccy=base.accy(ctx.author.id)+base.wpnaccy(ctx.author.id)
    db=sqlite3.connect('user.sqlite')
    c=db.cursor()
    combo=base.combo(ctx.author.id)
    if combo == None:
        c.execute("UPDATE user SET combo=? WHERE user_id=?",(1, ctx.author.id))
        db.commit()
        combo=base.combo(ctx.author.id)
    def check(m):
        return m.content.__contains__('SAO attack') and m.author == ctx.author.id
    try:
        msg = await cardinal.wait_for('message',timeout=1, check=check)
        combo=base.combo(ctx.author.id)
        c.execute("UPDATE user SET combo=? WHERE user_id=?",(combo+1, ctx.author.id))
        db.commit()
        combo=base.combo(ctx.author.id)
    except asyncio.TimeoutError:
        c.execute("UPDATE user SET combo=? WHERE user_id=?",(0, ctx.author.id))
        db.commit()
        combo=base.combo(ctx.author.id)
    idk=random.randint(1, 100)
    if arg == "test":
        if ctxatk-audef > 0 and combo < 3 and idk < ctxaccy:
            await ctx.send(f"{combo}連擊!\n你對{user.display_name}造成了{ctxatk-audef}點傷害")
            c.execute("UPDATE user SET hp=? WHERE user_id=?",(auhp-ctxatk-audef, ctx.author.id))
        elif ctxatk-audef>0 and combo >= 3 and idk < ctxaccy:
            await ctx.send(f"{combo}連擊!\n你對{user.display_name}造成了{ctxatk-audef}點傷害")
            c.execute("UPDATE user SET hp=? WHERE user_id=?",(auhp-ctxatk-audef, ctx.author.id))
        elif ctxatk-audef<0:
            await ctx.send(f"{user.display_name}擋住了!")
        elif idk > ctxaccy:
            await ctx.send(f"{ctx.author.display_name}眼殘打不中")
    else:
        await ctx.send("戰鬥系統測試中")
    db.commit()
@cardinal.command()
async def shop(ctx):
    sc=cardinal.get_channel(736559325631217754)
    if ctx.channel == sc:
        await ctx.send(file=discord.File('welcome.gif'))
        await asyncio.sleep(5)
        await ctx.send('我們有這些武具')
        await ctx.send(file=discord.File('buyweapon.png'))
        await ctx.send('如果你有意購買可以使用 SAO buy "武器名稱"')     
    else:
        await ctx.send("你來錯頻道了")
@cardinal.command()
async def buy(ctx, wpn):
    sc=cardinal.get_channel(736559325631217754)
    if ctx.channel == sc:
        try:
            db=sqlite3.connect('user.sqlite')
            c=db.cursor()
            c.execute(f'SELECT money FROM user WHERE user_id={ctx.author.id}')
            money=c.fetchone()[0]
            cmoney = money
            c.execute(f'SELECT item FROM user WHERE user_id={ctx.author.id}')
            item=c.fetchone()[0]
            if int(money) >= 100:
                if wpn == "新手長劍":
                    c.execute('UPDATE user SET money=?, item=? WHERE user_id=?',(int(money)-100, item+"新手長劍武\t", ctx.author.id))
                elif wpn == "新手錘子":
                    c.execute('UPDATE user SET money=?, item=? WHERE user_id=?',(int(money)-100, item+"新手錘子武\t", ctx.author.id))
                elif wpn=="風花劍":
                    c.execute('UPDATE user SET money=?, item=? WHERE user_id=?',(int(money)-100, item+"風花劍武\t", ctx.author.id))
            elif int(money) >= 50:    
                if wpn == "新手匕首":
                    c.execute('UPDATE user SET money=?, item=? WHERE user_id=?',(int(money)- 50, item+"新手匕首武\t", ctx.author.id))
                c.execute(f'SELECT money FROM user WHERE user_id={ctx.author.id}')
                money=c.fetchone()[0]
                if cmoney != money:
                    await ctx.send(f"購買{wpn}成功")
                else:
                    await ctx.send("沒有這武器喔,還有我把隨機對話移到另一個地方了")
            else:
                await ctx.send("沒珂爾還敢來啊 窮鬼")
            db.commit()
            await ctx.send(f"餘額:{base.money(ctx.author.id)}")
        except Exception as e:
            await ctx.send(e)
    else:
        await ctx.send("你來錯頻道了")
@buy.error
async def buy_on_error(ctx, error):
    await ctx.send("還敢抓bug啊")
@cardinal.command()
async def updateName(ctx):
    db=sqlite3.connect('user.sqlite')
    cursor=db.cursor()
    cursor.execute(f'UPDATE user SET username=? WHERE user_id=?',(ctx.author.display_name, ctx.author.id))
    db.commit()
    await ctx.send(f"名稱已更改成:{ctx.author.display_name}")
@cardinal.command()
async def equip(ctx, arg):
    db=sqlite3.connect('user.sqlite')
    cursor=db.cursor()
    cursor.execute(f'SELECT item FROM user WHERE user_id={ctx.author.id}')
    item=cursor.fetchone()[0]
    if base.wpn(ctx.author.id) == "拳頭" or base.wpn(ctx.author.id) == None:
        if item.__contains__(arg) and item.__contains__("武"):
            cursor.execute("UPDATE user SET wpn=? WHERE user_id=?",(f"{arg}", ctx.author.id))
            await ctx.send(f"成功裝備{arg}")
            if item.__contains__("新手長劍"):
                cursor.execute("UPDATE user SET wpnatk=?, wpnaccy=? WHERE user_id=?",(25,15,ctx.author.id))
            elif item.__contains__("新手錘子"):
                cursor.execute("UPDATE user SET wpnatk=? WHERE user_id=?",(100,ctx.author.id))
            elif item.__contains__("新手匕首"):
                cursor.execute("UPDATE user SET wpnatk=? WHERE user_id=?",(50, ctx.author.id))
            elif item.__contains__("風花劍"):
                cursor.execute("UPDATE user SET wpnatk=? WHERE user_id=?",(70, ctx.author.id))
            elif item.__contains__("聖劍EX咖喱棒"):
                cursor.execute("UPDATE user SET atk=? WHERE user_id=?",(100000000000, ctx.author.id))
        elif item.__contains__(arg):
            await ctx.send("這不是武器")
        else:
            await ctx.send("你沒有這武器")
    else:
        await ctx.send("你已經裝備了武器")
    db.commit()
@cardinal.command()
async def unequip(ctx):
    db=sqlite3.connect('user.sqlite')
    c=db.cursor()
    c.execute("UPDATE user SET wpn=?, arm=?, wpnatk=?, wpnaccy=? WHERE user_id=?",("拳頭", None,0,0,ctx.author.id))
    db.commit()
@crystaln.command()
async def shop(ctx):
    await ctx.send("隱身水晶暫時不能購買")
    await ctx.send(file=discord.File("crystal.png"))
    await ctx.send('如果有意購買可以輸入 NPCC buy "水晶名稱" ')
@crystaln.command()
async def buy(ctx,d):
    db=sqlite3.connect("user.sqlite")
    c=db.cursor()
    c.execute(f"SELECT item FROM user WHERE user_id={ctx.author.id}")
    item=c.fetchone()[0]
    c.execute(f"SELECT money FROM user WHERE user_id={ctx.author.id}")
    money = c.fetchone()[0]
    if int(money) >= 500:
        if d == "轉移水晶":
            c.execute("UPDATE user SET money=?, item=? WHERE user_id=?",(int(money)-500,item+"轉移水晶\t", ctx.author.id))
        if d == "回復水晶":
            c.execute("UPDATE user SET money=?, item=? WHERE user_id=?",(int(money)-500,item+"回復水晶\t", ctx.author.id))
        if d == "解毒水晶":
            c.execute("UPDATE user SET money=?, item=? WHERE user_id=?",(int(money)-500,item+"解毒水晶\t", ctx.author.id))
        await ctx.send("購買成功")
    elif int(money) >= 10000:    
        c.execute("UPDATE user SET money, item=? WHERE user_id=?",(int(money)-10000,item+"迴廊水晶\t", ctx.author.id))
        await ctx.send("購買成功")
    else:
        await ctx.send("沒珂爾還敢來,你真是勇敢")
@cardinal.command()
async def info(ctx, user:discord.User):
    id=user.id
    db=sqlite3.connect('user.sqlite')
    cursor=db.cursor()
    cursor.execute(f'SELECT * FROM user WHERE user_id={user.id}')
    get=cursor.fetchall()[0]
    wpnatk=base.wpnatk(user.id)
    wpnaccy=base.wpnaccy(user.id)
    wpn=base.wpn(user.id)
    if wpn == "拳頭" or wpn == None:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}\n命中率:{get[4]+base.wpnaccy(id)}\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:拳頭\n殺人數:{get[18]}")   
    elif wpnatk == 0 and wpnaccy != 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}\n命中率:{get[4]+base.wpnaccy(id)}(+{wpnaccy})\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(id)}\n殺人數:{get[18]}")        
    elif wpnatk != 0 and wpnaccy == 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}(+{wpnatk})\n命中率:{get[4]+base.wpnaccy(id)}\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(id)}\n殺人數:{get[18]}")
    elif wpnatk != 0 and wpnaccy != 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}(+{wpnatk})\n命中率:{get[4]+base.wpnaccy(id)}(+{wpnaccy})\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(id)}\n殺人數:{get[18]}")
@info.error
async def info_on_error(ctx, error):
    id=ctx.author.id
    db=sqlite3.connect('user.sqlite')
    cursor=db.cursor()
    cursor.execute(f'SELECT * FROM user WHERE user_id={ctx.author.id}')
    get=cursor.fetchall()[0]
    wpnatk=base.wpnatk(ctx.author.id)
    wpnaccy=base.wpnaccy(ctx.author.id)
    wpn=base.wpn(ctx.author.id)
    if wpn == "拳頭" or wpn == None:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}\n命中率:{get[4]+base.wpnaccy(id)}\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:拳頭\n殺人數:{get[18]}")   
    elif wpnatk == 0 and wpnaccy != 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}\n命中率:{get[4]+base.wpnaccy(id)}(+{wpnaccy})\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(ctx.author.id)}\n殺人數:{get[18]}")        
    elif wpnatk != 0 and wpnaccy == 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}(+{wpnatk})\n命中率:{get[4]+base.wpnaccy(id)}\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(ctx.author.id)}\n殺人數:{get[18]}")
    elif wpnatk != 0 and wpnaccy != 0:
        await ctx.send(f"{get[1]}的資訊:\nHP:{get[2]}/{get[17]}\n攻擊:{get[3]+base.wpnatk(id)}(+{wpnatk})\n命中率:{get[4]+base.wpnaccy(id)}(+{wpnaccy})\n防禦:{get[5]}\n珂爾:{get[14]}\n裝備武器:{base.wpn(ctx.author.id)}\n殺人數:{get[18]}")
@cardinal.command()
async def ping(ctx):
    await ctx.send(f'Cardinal: {round(cardinal.latency * 1000)}ms\n水晶大師: {round(crystaln.latency * 1000)}ms')
@cardinal.command()
async def giveMoney(ctx, arg, user:discord.User):
    try:
        gavemoney=int(arg)
        if gavemoney > 0:
            db=sqlite3.connect('user.sqlite')
            cursor=db.cursor()
            ctxmoney=base.money(ctx.author.id)
            usermone=base.money(user.id)
            cursor.execute("UPDATE user SET money=? WHERE user_id=?",(int(ctxmoney)-gavemoney, ctx.author.id))
            cursor.execute("UPDATE user SET money=? WHERE user_id=?",(int(usermone)+gavemoney, user.id))
            db.commit()
            await ctx.send("交易成功")
        else:
            await ctx.send("還想騙錢啊")
    except ValueError:
        await ctx.send("還想抓bug啊")
@cardinal.command()
async def system(ctx,*args):
    if ctx.author.id == 611418694245154847 and args[0] == "command":
        if args[1] == "手動輸入資料":
            db = sqlite3.connect("user.sqlite")
            cursor = db.cursor()
            sql = ("INSERT INTO user(user_id, username, hp, atk, accy, def, position, item, exp, level, guild, isGuildMaster,marryname, marryid, money, hplimit, killc, wpn) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            val = (args[2],args[3], 1000, random.randrange(30, 40), random.randrange(50, 100), random.randrange(10, 20), "起始之鎮", None,0, 0, None,0, None, None, 100, 1000, 0, "拳頭")
            cursor.execute(sql, val)
            db.commit()
            await ctx.send("系統通知:輸入資料完畢.")
        elif args[1] == "set":
            if args[2] == "NONE":
                db = sqlite3.connect("user.sqlite")
                cursor = db.cursor()
                cursor.execute(f"UPDATE user SET {args[3]}=? WHERE user_id=?",(None,args[4]))
                db.commit()
                await ctx.send(f"已更改OBJECTID:{args[4]} 資料:{args[3]}")
        elif args[1] == "DELETE":
            db = sqlite3.connect("user.sqlite")
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM user WHERE user_id=? AND username=?",(args[2], args[3]))
            db.commit()
            await ctx.send(f"已移除物體")                        
    else:
        await ctx.send("你沒有權限")

try:
    loop = asyncio.get_event_loop()
    loop.create_task(cardinal.start("我才不告訴你勒"))
    loop.create_task(crystaln.start("我才不告訴你勒"))
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()
    quit()