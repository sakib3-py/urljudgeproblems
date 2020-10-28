age_in_days = int(input())
age_in_years = age_in_days / 365 #1year=365days
remaining_days = age_in_days % 365
age_in_months = remaining_days / 30
remaining_days_2 = remaining_days % 30
print(f"{int(age_in_years)} ano(s) \n{int(age_in_months)} mes (es) \n{int(remaining_days_2)} dia (s)") 