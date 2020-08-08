import base
def inputvalue(author):
    level=base.level(author)
    exp=base.exp(author)
def lvlup(author):
    base.lvlup(author)
def lvl(author):
    if level == 0 and exp > 1:
        lvlup(author)
def lvlimit(levl):
    x=round(levl*100+levl/7)
    while str(x).endswith("0") == False:
        x+=1
    return x
def percentage1(percent, whole):
  return (percent * whole) / 100.0
def percentage2(part, whole):
  return 100 * float(part)/float(whole)
print(percentage1(20,595))
print(percentage1(20,595))