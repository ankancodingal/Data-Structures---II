# Check if Prime
from math import sqrt
number=int(input("Enter your number \n"))
if number>1:
  for i in range(2,int(sqrt(number))+1):
    if(number%i==0):
      print(number, " is not prime")
      break
  else:    
    print(number, " is prime")
else:
  print(number, "is not prime")

# ---------------------------------------------------
# Prime Sieve
def primeSeive(n):
    prime = [True for i in range(n + 1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1):
        if prime[p]:
            print(p)


n = int(input("Enter number to find all prime numbers less than the number : "))
primeSeive(n)
print ("Following are the prime numbers smaller.")
print ("than or equal to")
# -------------------------------------------------------------------------------
# 2 digit Primes
# Prime seive

def primeSeive(n):

    # Make list to store if number is prime or not     
    prime = [True for i in range(n + 1)]

    # Start from 2 as 1 and 0 are non prime
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        # If number is prime 
        if (prime[currentNumber] == True):
            # Mark all multiples of that number as non primes
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1

    # Mark 0,1 as non primes
    prime[0]= False
    prime[1]= False

    # Print all primes till n
    for p in range(n + 1):
        if prime[p]:
            print(p)


n = 99
print("All 2 digit prime numbers: ")
primeSeive(n)
