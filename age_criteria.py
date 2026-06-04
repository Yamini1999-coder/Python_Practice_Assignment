#Take a check if age> 60 print senior, if age>18 print adult, if age>10 print teen else child

age = int(input("Enter your age:"))
if age>60:
    print ("You are a senior sitizen")
elif age>18:
    print ("You are an adult")
elif age>10:
    print("You are a teen")
else:
    print("you are a child")