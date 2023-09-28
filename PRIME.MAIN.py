#Let user enter the numbers of their choice
print("Welcome to prime number probilities generator!")
numbers=[]
n =int(input("How many numbers are you testing?: "))
print("Please enter the numbers(one at a time): ")
#append input to a list based on n
for i in range(0,n):
    j=int(input())
    numbers.append(j)
#confirm input with user
print(" The numbers you entered are: ",numbers)
 

def probability_of_prime(a):
  c=0
  # here numbers is the list a
  total=len(a)
  for i in a:
    #funciton to see if its a prime or not
    if(i>1):
      c2=0
      for j in range(2,i):
        if(i%j==0):
          c2+=1
      if(c2==0):
        c+=1
  #probability value:
  probability=(c/total*100)
  print(str(probability) + "%")
print(probability_of_prime(numbers))