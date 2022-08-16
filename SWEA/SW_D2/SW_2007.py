T = int(input())
for test_case in range(1, T + 1):
    word = input()
    for i in range(len(word)):
        if word[0] == word[i] and word[1] == word[i+1]:
            if i>0:
                print(f'#{test_case} {i}')
                break