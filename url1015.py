import math

p_1 = input().split()
x1,y1 = p_1
p_2 = input().split()
x2,y2 = p_2
distance = math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)
print(f"{distance:.4f}")

