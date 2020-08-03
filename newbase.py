import sqlite3
db=sqlite3.connect('new.db')
c=db.cursor()
c.execute("INSERT INTO pstats(userid, username,hp,hplimit,atk,accy,def,walkspeed) VALUES(?,?,?,?,?,?,?,?)",("611418694245154847","testaccount",1000,1000,1000,100,1000,100))
db.commit()
def username(id):
    c.execute(f"SELECT username FROM pstats WHERE userid={id}")
    return c.fetchone()[0]
def hp_hplimit(id):
    c.execute(f"SELECT hp, hplimit FROM pstats WHERE userid={id}")
    return c.fetchone()[0]
id="611418694245154847"
print(username(id))