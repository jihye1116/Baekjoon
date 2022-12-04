# 과제 안 내신 분...?
students = [i for i in range(1, 31)]
for i in range(28):
    students.remove(int(input()))
# *연산자와 print()함수의 sep옵션    
print(*students, sep='\n')