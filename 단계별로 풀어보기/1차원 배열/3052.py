# 나머지
remainder = []
for i in range(10):
    remainder.append(int(input())%42) 
remainder = set(remainder) # set : 순서가 없고 중복이 없는 집합 자료형!
print(len(remainder))