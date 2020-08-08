import sqlite3
db=sqlite3.connect('user.sqlite')
c=db.cursor()
cursor=c
def username(author):
    c.execute(f'SELECT username FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def hp(author):
    c.execute(f'SELECT hp FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def hplimit(author):
    c.execute(f'SELECT hplimit FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def atk(author):
    c.execute(f'SELECT atk FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def accy(author):
    c.execute(f'SELECT accy FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def def_(author):
    c.execute(f'SELECT def FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def guild(author):
    c.execute(f'SELECT guild FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def guildOwner(author):
    c.execute(f'SELECT isGuildMaster FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def wpn(author):
    c.execute(f'SELECT wpn FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def agn():
    c.execute(f'SELECT guild FROM user WHERE isGuildMaster=1')
    return c.fetchall()
def money(author):
    c.execute(f'SELECT money FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def combo(author):
    c.execute(f'SELECT combo FROM user WHERE user_id = {author}')
    return c.fetchone()[0]
def wpnatk(author):
    c.execute(f'SELECT wpnatk FROM user WHERE user_id={author}')
    wa=c.fetchone()[0]
    if wa == None:
        return 0
    else:
        return wa
def wpnaccy(author):
    c.execute(f'SELECT wpnaccy FROM user WHERE user_id={author}')
    wa=c.fetchone()[0]
    if wa == None:
        return 0
    else:
        return wa
def combowait(author):
    c.execute(f'SELECT combowait FROM user WHERE user_id={author}')
    x=c.fetchone()[0]
    if x==None:
        return 0
    else:
        return 1
def killc(author):
    c.execute(f'SELECT killc FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def position(author):
    c.execute(f'SELECT position FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def exp(author):
    c.execute(f'SELECT exp FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def level(author):
    c.execute(f'SELECT level FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def item(author):
    c.execute(f'SELECT item FROM user WHERE user_id={author}')
    return c.fetchone()[0]
def lvlup(author):
    lvl=level(author)
    c.execute(f'UPDATE user SET level=? WHERE user_id=?',(level+1,author))
    db.commit()
def expplus(value, author):
    xp=exp(author)
    c.execute(f'UPDATE user SET exp=? WHERE user_id=?',(xp+value,author))
    db.commit()
595