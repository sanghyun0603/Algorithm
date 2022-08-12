mou =['a','e','i','o','u']
while True:
    s = input().lower()
    if s == '#':
        break
    counts = 0
    for i in s:
        if i in mou:
            counts += 1
    print(counts)