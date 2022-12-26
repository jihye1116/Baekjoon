# 크로아티아 알파벳
word = input()
count = 0

alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in alpa:
    word = word.replace(i, '*')
print(len(word))