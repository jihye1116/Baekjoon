# 오븐 시계
hour, min= map(int, input().split())
cooking = int(input())

hour += int(cooking /60)
min += cooking % 60

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24

print(hour, min)