"""Q3.Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
using for
range( )
range( start?, stop, step?)
Range functions returns a sequence of numbers, starting from 0 by default, and increments by
1 (by default), and stops before a specified number."""

# Define the list of numbers (squares of 1 to 10)
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Loop through each element in the list
for num in numbers:
    print(num)


my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49

# Initialize a flag to track if the number is found
found = False

# Loop through the tuple using range() to keep track of the index
for index in range (len(my_tuple)):
    if my_tuple[index] == x:
        print("Number found")
        found = True
        break # Stop the loop once the number is found

# If the loop finishes and 'found' is still False, the number isn't there
if not found:
    print("number not found")

# returns a sequence of number using range function starting with 0 and step size 1 till a specified number
for i in range (0,6,1):
    print(i)