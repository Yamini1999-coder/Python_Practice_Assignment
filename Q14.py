#Q14. Write a Python program to print all uppercase letters in a string using a for loop.

string = "Hello World! Welcome to Python Programming."

for char in string:
#check if the charecter is uppercase
    if char.isupper():
        print (char, end=" ") #prin all uppercase char in a same line  using end =" "