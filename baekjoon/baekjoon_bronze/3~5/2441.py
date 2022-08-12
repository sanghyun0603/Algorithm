stars = int(input())
for i in range(stars):
    if i == 0:
        print('*'*stars)
    else:
        print(' '*i +'*'*(stars-i))