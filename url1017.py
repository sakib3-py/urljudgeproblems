time_spentHours = int(input())
avarage_speed = int(input())
car_mileage = 12
total_distance = time_spentHours * avarage_speed
fuel_spent = total_distance / car_mileage
print(f"{fuel_spent:.3f}")