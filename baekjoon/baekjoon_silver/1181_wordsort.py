N = int(input())
words = []
sort_words = []
for i in range(N):
    word = input()
    if word not in words:
        words.append(word)
words.sort()
for j in range(1,51):
    for i in range(len(words)):
        if len(words[i]) == j:
            sort_words.append(words[i])
for i in sort_words:
    print(i)