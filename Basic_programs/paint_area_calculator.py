import math

def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover
  number_of_cans = math.ceil(number_of_cans)
  print(f"You'll need {number_of_cans} cans of paint.")


# Defining a function called paint_calc() so that the code below works.   


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


