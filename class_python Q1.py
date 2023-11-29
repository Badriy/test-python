class BankAccount:        
    def __init__(self,balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
        
    def deposit(self):
        deposi=int(input("Enter how much you will deposite:"))
        if deposi < 0 :
           return("Invalid input") 
        amou = self.__balance + deposi
        return(f"The amoun of the acount {self.__account_number} is  :", amou )
        
    def withdrawal(self):
        withdraw=int(input("Enter how much you will withdrawit:"))
        if withdraw < 0 :
           return("Invalid input") 
        if withdraw < self.__balance:
           amou = self.balance - withdraw 
           return amou
        else:
          return("The amount is not enogh for withdrawal")  
        
    def display_info(self):
        print("Acount Number :", self.__account_number)
        print("Acount Balnce:" , self.__balance )
        
b1 = BankAccount(100000, 8764321865789)
b1.display_info()
print(b1.deposit())
print(b1.withdrawal())