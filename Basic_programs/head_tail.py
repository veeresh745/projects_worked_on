# program to print head or tail randomly
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: ")) #ignore this thing, it's for online compiler to check
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
answer = random.randint(0, 1)
if answer == 0:
  print("Tails")
else:
  print("Heads")
