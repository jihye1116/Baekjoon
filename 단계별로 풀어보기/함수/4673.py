# 셀프 넘버

def d(n):
    n = n + sum(map(int, str(n)))
    return n

other = set()

for i in range(10001):
    other.add(d(i))

for j in range(10001):
    if j not in other:
        print(j)