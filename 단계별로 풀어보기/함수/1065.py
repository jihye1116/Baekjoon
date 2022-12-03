# 한수

n = int(input())
hansu = 0
for i in range(1,n+1):
    istr = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif istr[0]-istr[1] == istr[1]-istr[2]:
        hansu += 1
print(hansu)