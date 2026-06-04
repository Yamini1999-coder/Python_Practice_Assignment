# Q23. Write a Python program to print the Fibonacci sequence up to the 10th term using a while loop.

# Initialize the first two terms and a counter
n1, n2 = 0, 1
count = 0
max_term = 10

print("Fibonacci sequence up to the 10th term:")

# Loop until we have printed 10 terms
while count < max_term:
    print (n1 , end= " ")
    
    # calculate the next term
    nth = n1 + n2
    # Update the values for the next iteration
    n1 = n2
    n2 = nth

    # increment the counter
    count += 1