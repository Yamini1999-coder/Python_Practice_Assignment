"""Q2. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value"""

# start with the empty dictionary
Marks_dict = {}
# loop 3 timed to get input for 3 subjects
for i in range (1,4):
    Subject = input ("Enter subject name:")
    Marks = float(input("Enter the marks:"))
    # add Subject(key) and Marks (value) to the dictionary
    Marks_dict[Subject] = Marks
# print final dictionary
print (Marks_dict)