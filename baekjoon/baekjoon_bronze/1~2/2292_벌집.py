N = int(input())
num =1
room = 1
while True:
    if N == 1:
        room = 1
        break
    elif N <= num:
        break
    num += 6*room
    room +=1
print(room)