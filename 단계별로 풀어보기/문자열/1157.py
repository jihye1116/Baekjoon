# 단어 공부
word = input().lower()
alpha = list(set(word))
cnt = []
for i in alpha:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(alpha[(cnt.index(max(cnt)))].upper())