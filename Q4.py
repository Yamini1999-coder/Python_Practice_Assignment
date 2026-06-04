"""Q4. Print numbers from 1 to 100.
Print numbers from 100 to 1.
Print the multiplication table of a number n.
using for & range( )
pass Statement
pass is a null statement that does nothing. It is used as a placeholder for future code.
generally used in execption handling
for el in range(10):
pass"""

# Print a numbers from 1 to 100
for i in range (1,100+1, 1):
    print(i)

# Print a numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a number n.
n=10
for el in range(1,11,1):
    i=n*el
    print(i)

# pass function
for el in range(1,10):
    pass

#write a table from 1-10

for n in range (1,11):
    for i in range (1,11):
        res = n * i
        print(f"{res}\t", end = " ")
    print() # Next row