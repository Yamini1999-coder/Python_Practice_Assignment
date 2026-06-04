# Q12 Write a Python program to find the largest number in a list using a for loop.

numbers = [2,5,6,8,11,15]
largest_num = numbers[0]

for num in numbers:
    if num > largest_num:
        largest_num = num
print ("the largest number in a list is:", num)
