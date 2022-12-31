# 손익분기점
A,B,C = map(int, input().split()) # A: 고정 비용, B: 가변 비용, C: 노트북 가격, n: 노트북 대수
if B>=C: 
    print("-1") # 가변 비용이 노트북 가격보다 클 때
else: 
    print(A//(C-B)+1) # 판매수입: A+nB=nc  -> n(B+C)=A  -> ∴ n=A/(B+C) 