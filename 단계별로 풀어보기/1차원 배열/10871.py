# x보다 작은 수
n, x = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(n):
    if numbers[i] < x: print(numbers[i], end=" ")