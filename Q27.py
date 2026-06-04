# Q27. Write a Python program to print numbers from 1 to 10 and stop the loop when a number divisible by 4 is encountered using break.

# using for loop
for i in range (1,11):
    if i%4 == 0:
        break
    print(i)

# using while loop
i = 1
while i<= 10:
    if i%4 == 0:
        break
    print(i)
    i += 1
