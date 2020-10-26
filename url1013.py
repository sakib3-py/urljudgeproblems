user_input = input().split()
a,b,c = user_input
maiorab =(int(a) + int(b) + abs(int(a)-int(b))) / 2
result = (int(maiorab) + int(c) + abs(int(maiorab)-int(c))) / 2
print(f"{int(result)} eh o maior")