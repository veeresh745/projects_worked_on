#Print the score, based on some logical calculations.
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# combining both the names
combined_string = lower_name1 + lower_name2

#counting true
t = combined_string.count("t")
r = combined_string.count("r")
u= combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e

#counting love
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v +e

#score concatenation as a string
score_conc = str(true) + str(love)

#score conversion as a intege for further comparison
score = int(score_conc)

#comparing the score and printing
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")
