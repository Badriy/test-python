#+968 9626-222
om_number="968"
num=input("Enter your phone number:")
if(num[0] == "+" ):
   if((num[1:4]) in om_number):
       if(len(num)==12 and num[1:13].isdigit()):
           print(num[0:4]+" "+num[5:9]+"-"+num[8:12])
       else:
          print("The number is wrong ")
   else:
      print("The number is wrong , you must start with +968")
else:
   print("The number is wrong , you must start with +")          