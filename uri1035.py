a,b,c,d = map(int,input().split())
sum_1 = c + d
sum_2 = a + b
if b>c and d>a and sum_1 > sum_2 and c > 0 and a % 2 == 0 :
    print("Valores aceitos")
else:
    print("Valores nao aceitos")