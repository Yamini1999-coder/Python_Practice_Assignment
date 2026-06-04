#Q25. Write a Python program to print numbers from a list until a negative number is encountered using a while loop

list = [10, 20, 30, 35, -5, 40, 50]

index = 0

while index < len(list):
    # Check if the current number is negative
    if list[index] < 0 :
        break   # Exit the loop immediately
    print (list[index])
    index += 1
