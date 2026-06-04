# code to  display wheather a person is eligible to vote or not
age = int(input("Enter your age:"))
citizen = input("are you citizen(yes/no):").strip().lower()=="yes"
if age>18 and citizen:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

