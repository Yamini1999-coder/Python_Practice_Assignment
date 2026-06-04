# take a user input and print its type whether its str, int or float
User_input = input("Enter something:")
# try to converting to int first
try:
    val = int(User_input)
    print("Type :  int")
except ValueError:
# if not int then try to converting to float
    try:
        val = float(User_input)
        print ("Type: Float")
    except ValueError:
        # if not int and float then trated it as string
        print ("Type : Str")