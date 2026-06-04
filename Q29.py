# Q29. Write a Python program to print numbers from 1 to 10 and break the loop when an even number is encountered, using a for loop with an else clause.

print("Starting the loop:")

# Loop through numbers from 1 to 10
for num in range(1, 11):
    # Check if the number is even
    if num % 2 == 0:
        print(num, "- Even number found! Breaking out of the loop.")
        break  # Instantly exits the loop
        
    print(num, "- Odd number")
else:
    # This block only runs if the loop completes naturally without hitting a 'break'
    print("The loop finished all iterations without encountering a break.")

print("Program ended.")