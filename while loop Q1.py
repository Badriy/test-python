#how to get te sum of entered number as integer:
i = 0
n = input("Entr number :")
sum_= 0
while(n!=0):
     sum_+=int(n)%10
     n= int(n)//10
    
print (sum_)

