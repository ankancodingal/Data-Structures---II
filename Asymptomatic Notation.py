# O(1) Time
def printnumber(n):
  literation = 0
  print("the total number entered my user is",n)
  literation+=1
  print("total literation done by computer is",literation,"\n")
printnumber(10)
printnumber(200)
print("\n with any 'n' the time taken by the computer will not change")
# --------------------------------------------------------------------------------
# O(n) Time
def OnTime(n):
  iteration=0
  for i in range(1,n+1):
    iteration+=1
  print("When n is ",n," Iterations = ",iteration)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nWith every 'n' the time taken and iterations will increase linearly")
# -------------------------------------------------------------------------------------
# O(n^2) Time
def test(n):
  iteration = 0
  for i in range(0,n):
    for j in range(0,n):
      print("*",end="")
      iteration+=1
    print("")
  print("\nwhen n is",n,"iteration =",iteration)
test(5)
test(4)
test(3)

print("\n with every 'n' the taken = n^2")
print("(n^2)")
# --------------------------------------------------------------------------------------
# Loop Time
# Program to print the time complexity of the given function

# Given function
def myfunction(n):
  # Loop 1  
  for i in range(0,n+1):
      print("First Loop")

  # Loop 2
  j=1
  while(j<=n+1):
      print("Second Loop ",j)
      j=j*2

  # Loop 3
  for i in range(0,100):
      print("Third loop")

print("Function above will take time :")
print(" O(N) +  O(log N) + O(1)")
