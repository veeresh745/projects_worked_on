#program to print human life in weeks.
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left = 90 - int(age)
months = left * 12
days = left * 365
week = left * 52



print(f"You have {days} days, {week} weeks, and {months} months left.")



