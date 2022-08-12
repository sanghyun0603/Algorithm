score_list = []
for i in range(5):
    score = int(input())
    if score < 40 :
        score_list.append(40)
    else:
        score_list.append(score)
print(int(sum(score_list)/len(score_list)))