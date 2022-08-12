station = []
for i in range(4):
    a = list(map(int,input().split()))
    station.append(a)
maxs = 0
person = 0
for i in station:
    person -= i[0]
    person += i[1]
    if maxs < person:
        maxs = person
print(maxs)