# Q15 Write a Python program to count the number of vowels in a string using a for loop

input_str = "Hello World! Welcome to Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input_str:
    if char in vowels:
        vowel_count +=1
print ("Total count of vowels is: ",vowel_count)