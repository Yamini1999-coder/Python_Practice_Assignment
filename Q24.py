# Q24. Write a Python program to find common elements between two lists using a for loop.

list1 = [10, 20, 25, 30, 40, 50]
list2 = [25, 33, 36, 40, 55, 60]

common_element = []

for items in list1:
    if items in list2 and items not in common_element:
        common_element.append(items)
print ("Common elements are: ", common_element)
