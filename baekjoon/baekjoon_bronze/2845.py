per, area = map(int,input().split())
arti_li = list(map(int,input().split()))
person = per * area
for i in range(len(arti_li)):
    arti_li[i] -= person
print(*arti_li)