import math
vac = int(input())
korea =int(input())
mathm = int(input())
ko_pg = int(input())
ma_pg = int(input())
sty = korea/ko_pg
sty_m = mathm/ma_pg
va = max(sty,sty_m)
if va - math.trunc(va) == 0 :
    print(vac - va)
else:
    print(int(vac - (math.trunc(va))-1))