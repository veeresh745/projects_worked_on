# program to print average height of the Student
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
for i in range (n+1):
  sum = sum + student_heights[i]
avg = sum / (n+1)
avg = round(avg)
print(avg)



