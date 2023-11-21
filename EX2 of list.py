num= (input("Enter the number : "))
result=[]
if num.upper()  != "Q":
     for i in num:
        result.append(int(i))
     print(result)
else :
   print("End")