h1=int(input(" enter hour for first time :"))
m1=int(input("enter mint for first time :"))
priod1=input("enter am or pm for first time :")

h2=int(input(" enter hour for second time :"))
m2=int(input("enter mint for second time :"))
priod2=input("enter am or pm for second time :")

 if(priod1 == "am" and priod2 =="pm"):
    print ("first time is first :"+ str(h1)+":"+str(m1)+priod1)
 elif (priod2 == "am" and priod1 =="pm"):
      print ("second time is first :"+ str(h2)+":"+str(m2)+priod2)
 else:
     if (h1 < h2):
        print("first time is first :"+ str(h1)+":"+str(m1)+priod1)
        
     elif (h1 == h2):
         if (m1<= m2):
          print("first time is first :"+ str(h1)+":"+str(m1)+priod1)
          
         else:
            print ("second time is first :"+ str(h2)+":"+str(m2)+priod2) 
     else:
         print ("second time is first :"+ str(h2)+":"+str(m2)+priod2)
   

    
    
