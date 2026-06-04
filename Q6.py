#Q 6 Write a Python program to calculate the sum of numbers from 1 to 10 using a for loop

total_sum = 0
i=1
for i in range(1,10+1,1):
    total_sum += i
    i += 1
    
print (f"Sum of numbers from 1 to 10 is: {total_sum}")