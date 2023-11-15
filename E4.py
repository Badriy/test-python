#write program that simulates a simple ATM , the program should ask the user fo their pin , and if its correct , allow them to check balance , withdraw money or deposit money
pin2=int(input("enter your pin number:"))
PIN= 1234
BALANCE = 20000

if(pin2==PIN):
    print("1. check balance\n2. withdraw\n3. deposit")
    choice = int(input("enter your choice: "))
    if (choice  == 1):
        print("your balance is: " , str(BALANCE) )
    elif (choice == 2):
        amount = float(input("enter your amount: "))
        BALANCE = BALANCE - amount
        print ("your balance is: " , str(BALANCE)) 
    elif (choice == 3):
        amount = float(input("enter your amount: "))
        BALANCE = BALANCE + amount
        print ("your balance is: " , str(BALANCE)) 
        
    else:
        print("try again")
        
else:
    print("your PIN is wrong")