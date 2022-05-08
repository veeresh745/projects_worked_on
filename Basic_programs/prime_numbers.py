#defining a function called prime_checker() 
# so that the code below works.
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("Prime number")
  else:
    print("Not a prime number")

#this is the input line for the user to enter a number
n = int(input("Check this number: "))
prime_checker(number=n)



