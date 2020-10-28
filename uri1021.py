x = float(input())
print("NOTAS:")
a = x / 100
print(f"{int(a)} nota(s) de R$ 100.00")
remain = x % 100
b =  remain / 50
print(f"{int(b)} nota(s) de R$ 50.00")
remain_1 = remain % 50
c = remain_1 / 20
print(f"{int(c)} nota(s) de R$ 20.00")
remain_2 = remain_1 % 20
d = remain_2 / 10
print(f"{int(d)} nota(s) de R$ 10.00")
remain_3 =  remain_2 % 10
e = remain_3 / 5
print(f"{int(e)} nota(s) de R$ 5.00")
remain_4 = remain_3 % 5
f = remain_4 / 2
print(f"{int(f) } nota(s) de R$ 2.00")
print("MOEDAS:")
remain_5 = remain_4 % 2
g = remain_5 / 1
print(f"{int(g)} moeda(s) de R$ 1.00")
remain_6 = remain_5 % 1
h = remain_6 / 0.50
print(f"{int(h)} moeda(s) de R$ 0.50")
remain_7 = remain_6 % 0.50
i = remain_7 / 0.25
print(f"{int(i)} moeda(s) de R$ 0.25")
remain_8 = remain_7 % 0.25
j = remain_8 / 0.10
print(f"{int(j)} moeda(s) de R$ 0.10")
remain_9 = remain_8 % 0.10
k = remain_9 / 0.05
print(f"{int(k)} moeda(s) de R$ 0.05")
remain_10 = remain_9 % 0.05
l = remain_10/0.01
print(f"{int(round(l))} moeda(s) de R$ 0.01")



