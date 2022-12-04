# 평균은 넘겠지
n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    avg = sum(numbers[1:])/numbers[0]
    sangtachi = 0
    for j in numbers[1:]:
        if j > avg:
            sangtachi += 1
    print(f'{sangtachi/numbers[0] *100:.3f}%')
