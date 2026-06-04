"""Q5 WAP to find the sum of first n numbers. (using while)
WAP to find the factorial of first n numbers. (using for)"""

n = int (input("Enter a number:"))

#total_sum of first n numbers using while loop

# Initialize the sum and the counter loop variable
total_sum = 0
i=1
# Use a while loop to iterate from 1 to n
while i <= n:
    total_sum += i # Add the current number to the total sum
    i +=1  # Increment the counter to move to the next number
print(f"total_sum of first {n} number is:{total_sum}") 

# WAP to find the factorial of first n numbers. (using for)

def find_factorial (n):
    if n <= 0:
        print ("Please enter positive number")
        return

    factorial = 1

    for i in range (1, n+1, 1):
        factorial *= i
        print (f"factorial  of {i} is: {factorial}")

find_factorial(n)