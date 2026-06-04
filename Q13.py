# Q13. Write a Python program to find the average of numbers in a list using a for loop.

numbers = [1,2,3,4,5]
total_sum = 0
for num in numbers:
    total_sum += num
average= total_sum / len(numbers)
print("average of a given numbers is: ", average)