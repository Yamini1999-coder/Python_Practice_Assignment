"""Q1 Store following word meanings in a python dictionary :
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”, “java”,“C++”,“python”,“javascript”,“java”,“python",“java”,“C++",“C”
table : “a piece of furniture”,“list of facts & figures”, cat : “a small animal"""

# create the dictionary with the words and their meaning
word_meaning = {
                "table" : ["a piece of furniture, list of facts & figures"],
                "cat" : ["a small animal"]
                }

# print the word with their meanings
print ("Meaning of given word is:",word_meaning)

# start with the list of subjects we are having
list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# use len() to get count for each subject and set () for unique set of subject
classroom_needed = len (set(list))

# print the  total nuber of classrooms needed for each subject
print("The number of classrooms needed for all subjects are:",classroom_needed)
