import math
try:

    a,b,c = map(float,input().split())
    x = -b + (math.sqrt((b**2) - 4*a*c))
    y = -b - (math.sqrt((b**2) - 4*a*c))
    x_1 = x / (2*a)
    x_2 = y /(2*a)
    print(f"R1 = {x_1:.5f}\nR2 = {x_2:.5f}")
except:
    if ValueError or ZeroDivisionError:
        print("Impossivel calcular")
    
    
