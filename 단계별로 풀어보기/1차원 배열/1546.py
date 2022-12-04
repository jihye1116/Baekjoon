# 평균
n = int(input())
numbers = list(map(int, input().split()))
good = max(numbers)
sum = 0
for i in range(n):
    numbers[i] = numbers[i]/good*100
    sum += numbers[i] 
print(sum/n)