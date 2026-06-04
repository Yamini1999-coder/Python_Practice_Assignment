# Q16. Write a Python program to print a right-angled triangle pattern of stars using nested for loops.

# right-angled triangle pattern of stars
rows = 5
# Outer loop for the number of rows
for i in range (1,rows+1):

    # Inner loop for printing stars in each row
    for j in range (1,i+1):
        print("*" , end=" ")

    # Print a newline character to move to the next row
    print()
