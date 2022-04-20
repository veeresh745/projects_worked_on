#calculate the sum of even numbers from 1 to 100 including 1 and 100
#Write your code below this row 👇
sum = 0
for i in range(1, 101):
  if i % 2 == 0:
    sum = sum + i
    print(i)
print(sum)