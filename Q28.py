# Q28. Write a Python program to print odd numbers from 1 to 10 using a for loop and continue, and display a message when the loop completes. 

print ("The odd numbers in between 1 to 10 is : ")

for i in range (1,11):
    if i%2 == 0:
        continue
    print (i)

print ("The loop is completed successfully!")