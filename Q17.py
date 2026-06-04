# Q17 Write a Python program to calculate the factorial of a number using a while loop.

def find_factorial(n):

    if n<1:
        print ("Please enter the positive nummber")

    factorial = 1
    i = 1
    
    while i<n:
        factorial *= i
        print (f"Factorial of {i} is: {factorial}")
        i+=1
find_factorial(5)