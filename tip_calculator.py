print("Welcome to the tip calculator!")
amount = input("What was the total bill?")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

tip_calc = (float(amount) * float(tip)) / 100
tip_float = float(tip_calc)
total_amount = (float(amount) + tip_float)/int(people)
final = round(total_amount, 2)

print(f"Each person will pay {final}")
