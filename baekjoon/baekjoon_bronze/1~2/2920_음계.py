dajang = input().split()
dajang = ''.join(dajang)
if dajang == '12345678':
    print('ascending')
elif dajang == '87654321':
    print('descending')
else:
    print('mixed')