#ATM
card = input("Please insert your card (yes/no):").lower().strip()
if card == "yes":
    PIN = int (input ("Enter your PIN:"))
    if PIN == 1234:
        balance = 5000
        amount = int (input ("Enter the amount:"))
        if amount<= 5000:
            print ("Cash dispensed")
        else:
            print("Insufficient balance")
    else:
        print ("Invalid password")
else:
    ("Please insert your card")