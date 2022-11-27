# OX퀴즈
n = int(input())

for i in range(n):
    sum = 0
    score = 0
    ox = input()
    for j in ox:
        if j == 'O':
            score += 1
            sum += score
        else: score = 0
    print(sum)