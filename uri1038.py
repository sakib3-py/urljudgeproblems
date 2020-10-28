price = [0,4.00,4.50,5.00,2.00,1.50]
code = [price[1],price[2],price[3],price[4],price[5]]

x , y = map(int,input().split())
x = x-1

x = code[x]
print(x)
calculation = x * y
print(f"Total: R$ {calculation:.2f}")