# 더하기 사이클
n = int(input())
cycle = 1
newn =  (n%10)*10 + (int(n/10)+n%10)%10
while(True):
    if newn == int(n): break
    cycle +=1
    newn =  (newn%10)*10 + (int(newn/10)+newn%10)%10
print(cycle)