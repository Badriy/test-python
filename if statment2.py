#write program to calculate te discount o shopping cart based o the total amount is grater than $100,
#apply a 10% discount , otherwise apply a 5% discount. 
total_amount=int(input("enter amount:"))
if (total_amount > 100):
   discount=total_amount *10/100
else :
    
    discount=total_amount *5/100
    
print("the discount is :" total_amount-discount)