user_input = input().split()
pi = 3.14159
A,B,C = user_input
rec_triangle = (1/2 )* float(A)*float(C)
area_radius_circle = pi * float(C)**2
area_of_trapizium =  ((float(A)+float(B))*float(C))/2
area_of_square = float(B)**2
area_of_rectangle = float(A)*float(B)
print(f"TRIANGULO: {rec_triangle:.3f}")
print(f"CIRCULO: {area_radius_circle:.3f}")
print(f"TRAPEZIO: {area_of_trapizium:.3f}")
print(f"QUADRADO: {area_of_square:.3f}")
print(f"RETANGULO: {area_of_rectangle:.3f}")
    