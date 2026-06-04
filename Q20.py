# Q20. Write a Python program to find all prime numbers between 1 and 50 using nested for loops and if statements.

def get_prime():
    print ("The Prime numbers in between 1-50 is :")
    for num in range(2,51):
        for i in range(2,num):
                if (num % i) == 0:
                    break
        else:
            print(num , end=" ")
get_prime()


# one more way to find prime number is
import math
print ("The Prime numbers in between 1-50 is :")
for num in range (2,51):
     is_prime = True
     
     for i in range (2,num):
      if num % i == 0:
        is_prime = False
        break
      
    # If no factors were found, the number is prime 
     if is_prime:
      print (num, end = " ")