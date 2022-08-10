N1= int(input())
N2 = list(map(int,list(input())))
thr,fou,five,sums= 0,0,0,0
thr = N1 * N2[2]
fou = N1 * N2[1]
five = N1 * N2[0]
sums = thr + (fou*10) + (five*100)
print(thr)
print(fou)
print(five)
print(sums)

