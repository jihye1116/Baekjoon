# 킹, 퀸, 룩, 비숍, 나이트, 폰
need = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))
for i in range(6):
    print(need[i]-chess[i],end=' ')
