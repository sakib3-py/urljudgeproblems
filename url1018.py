x = int(input())
print(x)
a = x / 100
print(f"{int(a)} nota(s) de R$ 100,00")
remain = x % 100
b =  remain / 50
print(f"{int(b)} nota(s) de R$ 50,00")
remain_1 = remain % 50
c = remain_1 / 20
print(f"{int(c)} nota(s) de R$ 20,00")
remain_2 = remain_1 % 20
d = remain_2 / 10
print(f"{int(d)} nota(s) de R$ 10,00")
remain_3 =  remain_2 % 10
e = remain_3 / 5
print(f"{int(e)} nota(s) de R$ 5,00")
remain_4 = remain_3 % 5
f = remain_4 / 2
print(f"{int(f) } nota(s) de R$ 2,00")
remain_5 = remain_4 % 2
g = remain_5 / 1
print(f"{int(g)} nota(s) de R$ 1,00")