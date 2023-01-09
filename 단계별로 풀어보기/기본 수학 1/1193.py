# 분수찾기
n = int(input())

line = 1

while n > line:
    n -= line   # x = 14, 13, 11, 8, 4
    line += 1   # line = 1, 2, 3, 4, 5

if line%2 == 0:
    print(f"{n}/{line-n+1}")
else:
    print(f"{line-n+1}/{n}")
