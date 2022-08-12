words = input().upper()
word_dict = {}
for i in range(len(words)):
    if words[i] not in word_dict :
        word_dict[words[i]] = 1
    else:
        word_dict[words[i]] += 1
maxs = max(word_dict.values())
max_cnt = 0
for i in word_dict:
    if maxs == word_dict[i]:
        max_idx = i
        max_cnt +=1
if max_cnt >1:
    print('?')
else:
    print(max_idx)
