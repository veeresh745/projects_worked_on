#treasure map, guess and fill
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#i have splitted the position to get horizontal and vertical postion
position = int(position)
x = position / 10
x_int = int(x)
y = position % 10

#since index starts from 0 i have to substract 1 from x and y
if y-1 == 0:
  row1[x_int-1] = "X"
elif y-1 == 1:
  row2[x_int-1] = "X"
else:
  row3[x_int-1] = "X"

  #Easier way
#if suppose position is 23 then
# horizontal = int(position[0]) #2
# vertical = int(position[1])   #3

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
