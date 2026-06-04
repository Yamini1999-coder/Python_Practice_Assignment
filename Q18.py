# Q18 Write a Python program to find the first occurrence of a given number in a list using a while loop

def find_first_occurance(my_list , target_num):
    index = 0
    list_len = len (my_list)
    
    while index < list_len:
        if my_list[index] == target_num:
            return index
        index +=1
    return -1


my_list = [10, 20, 25, 30, 40, 45, 50]
target_num = 25
result = find_first_occurance (my_list, target_num)

if result != -1:
    print (f"The fist occurance of {target_num} is at index {result}")
else:
    print (f"{target_num} not found in a list")