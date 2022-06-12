#program to help you decide who is going pay the bill.
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# pay_bill = random.choice(names)

#Another method
#Get the total number of items in list.
num_items = len(names)

#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
person_pay = names[random_choice]


print(f"{person_pay} is going to buy the meal today!")
