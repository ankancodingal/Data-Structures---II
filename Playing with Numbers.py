# Palindrome Number
# Program to check if the given number is a palindrome 


# Take input from the user
number = int(input("Enter your Number : "))


# Store the number for comparision later 
store  = number
reverse=int(0)


# while number is not 0 all last digit to reverse number
while(number>0):
  rem = (number%10)
  reverse = reverse*10 + rem
  number//=10


# Print reversed number
print("\nReversed number : ",reverse)


# Check if palindrome or not
if(store==reverse):
  print("\nPalindrome")
else:
  print("\nNot palindrome")
# ----------------------------------------------------------------------
# GCD
numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)
# -------------------------------------------------------------------
	# Least Common Multiple
# Program to find HCF/GCD

# Using Eucliden Algorithms 
def hcf(numberSmallest,numberLargest): 
  while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
  return numberLargest

# Enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

# LCM equals product of numbers divide hcf of the numbers
lcm = int((numberSmallest / hcf(numberSmallest,numberLargest))* numberLargest)
print("LCM is : ",lcm)



