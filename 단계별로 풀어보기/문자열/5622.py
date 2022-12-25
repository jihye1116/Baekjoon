# 다이얼
alpa = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = list(input())

time = 0
for i in word:
    for j in alpa:
        if i in j:
            time += alpa.index(j) + 3
print(time)