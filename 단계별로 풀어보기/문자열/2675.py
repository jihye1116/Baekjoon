# 문자열 반복
n = int(input())
for i in range(n):
    c, S = input().split()
    for j in S:
        print(j*int(c), end="")
    print()