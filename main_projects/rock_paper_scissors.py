import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_chose = random.randint(0,2)

# iam doing this program using functions
#using function to check the conditions
def user_choice():
  print("You Chose:")
  if choice == 0:
    print(rock)
  elif choice == 1:
    print(paper)
  elif choice == 2:
    print(scissors)
  else:
    print("Invalid Choice")

#Relating numerical choices to string onees
def computer_choice():
  print("Computer Chose:")
  if computer_chose == 0:
    print(rock)
  elif computer_chose == 1:
    print(paper)
  elif computer_chose == 2:
    print(scissors)
  else:
    print("Invalid Choice")
  
#here we are printing the result
def result():
  if choice == 0 and computer_chose == 2:
    print("You Win")
  elif choice == 1 and computer_chose == 0:
    print("You Win")
  elif choice == 2 and computer_chose == 0:
    print("You Win")
  elif choice == computer_chose:
    print("draw")
  else:
    print("You Lose")
  
#calling all the functions
user_choice()
computer_choice()
result()
