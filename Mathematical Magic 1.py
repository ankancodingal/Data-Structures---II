# Strong Arms
number = int(input("Input number:"))
result = 0
temp = number
while temp!=0:
  digit = temp % 10 
  result = result+digit**3
  temp = temp//10
print(result)
if number == result:
  print(number, "is an armstrong number ")
else:
  print(number, "is not an armstrong number ")

# ---------------------------------------------------------
# That's a fact
number = int(input("Input number:"))
s = 0
temp = number

while temp!=0:
  digit = temp%10
  s = s+digit**3
  temp = temp//10
if number == s:
  print(number, "is an armstrong number ")
else:
  print(number, "is not an armstrong number ")

# ----------------------------------------------------------------
# Roman to Int

def roman_to_int(a):
  roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  int_form=0
  for i in range(len(a)):
    if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
      int_form-=roman[a[i]]
    else:
      int_form+=roman[a[i]]
  return int_form

a=input("enter a roman numeral")
print("interger form of",a,"is",roman_to_int(a))
# --------------------------------------------------------------------------
# Binary To Decimal
# Program to convert Binary to decimal 
 
def binaryToDecimal(binary):
    
    # Variable set as 0
    decimal, i = 0, 0

    # while there is a digit multiply with 2 power i 
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10

        # increment i
        i += 1
    print("Decimal : ",decimal)   
     

# Take binary input from the user 
binary = int(input("Enter your Binary: "))

# Call function
binaryToDecimal(binary)
