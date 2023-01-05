# 벌집
# 13 -> 3, 58->5
n = int(input())
bees_home = 1
cnt = 1
while n > bees_home :
    bees_home += 6 * cnt
    cnt += 1
print(cnt)