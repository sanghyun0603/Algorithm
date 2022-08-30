import sys
N = int(input())
people =[]
for i in range(N):
    a,b =sys.stdin.readline().split()
    a= int(a)
    people.append([a,b])
people.sort(key=lambda x:x[0])
for i in people:
    print(i[0],i[1])