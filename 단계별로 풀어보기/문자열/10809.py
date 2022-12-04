# 알파벳 찾기

S = input()
 
for i in range(ord('a'),ord('z')+1):
    if(ord(j) == i):
            print(S.index(j), end=" ")
    else:
        print(-1, end=" ")

# a = list(map(int, input().split()))
# print(len(a))