        response = requests.get(user.avatar_url)
        img = Image.open(BytesIO(response.content), 'r')
        img=img.resize((144, 144))
        name=base.username(user.id)
        chinese=ImageFont.truetype('msyh.ttc',28)
        saofont=ImageFont.truetype('SAOUITT-Regular.ttf',28)
        background = Image.open('test.png', 'r')
        draw=ImageDraw.Draw(background)
        pdata=[f'{base.hp(user.id)}/{base.hplimit(user.id)}',f'{base.atk(user.id)+base.wpnatk(user.id)}(+{base.wpnatk(user.id)})',f'{base.accy(user.id)+base.wpnaccy(user.id)}(+{base.wpnaccy(user.id)})',f'{base.def_(user.id)}',f'{base.money(user.id)}',f'{base.killc(user.id)}']
        chinesew=""
        for n in re.findall(r'[\u4e00-\u9fff]+', name):
                chinesew+=n
        if chinesew=="": 
                draw.text((185,75),name,font=saofont,fill="white")
        else: 
                draw.text((185,75),name,font=chinese,fill="white")
        draw.text((100,250),pdata[0],font=saofont,fill="white") #hp
        draw.text((100,290),pdata[1],font=saofont,fill="white") #atk
        draw.text((100,330),pdata[2],font=saofont,fill="white") #accy
        draw.text((100,370),pdata[3],font=saofont,fill="white") #def
        draw.text((100,410),pdata[4],font=saofont,fill="white") #cor(money)
        draw.text((100,450),pdata[5],font=saofont,fill="white") #kill count
        wanted=base.exp(user.id)
        if wanted > 0:
                im=Image.open('bar.png','r') 
                offset = (482,18)
                im=im.resize((18,wanted))
                background.paste(im, offset)
        else:
                pass        
        offset = (19,22)
        background.paste(img, offset)
        background.save('get.png')
        await ctx.send(file=discord.File('get.png'))