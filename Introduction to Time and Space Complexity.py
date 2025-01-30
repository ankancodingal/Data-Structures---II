# One Algo Three Faces
def fun1(n):
  return n*(n+1)/2
print(fun1(4))
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(i, i+1):
        sum += 1
      return sum
# -------------------------------------
# Multiply By N
# Program to find multiple with 1 and N iterations

# For 1 iteration simply multiply 
def o1(n,m):
  total = n*m
  print("\n1 iteration: ",total) 

# For N iteration run a for loop
def oN(n,m):
  total = 0
  for i in range(1,n+1):
    total += m
  print("N iteration: ",total) 

m = int(input("Enter 'a' for a*b : "))
n = int(input("Enter 'b' for a*b : "))

o1(m,n)
oN(m,n)

  
  
