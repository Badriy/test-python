#5!
#1*2*3*4*5

#n = 5
#f = 1
#for i in range(1,n+1):
#    if(i != n):
#         print(i, end = " x ")
#    else:
#        print(i)
        
#    f *= i
#print()
#print(f)


#whil loop
n = 5
f = 1
i = 1
while (True):
    if(i != n):
       print(i, end = " x ")
    else:
        print(i) 
    f *= i
    i +=1
    if(i == n+1):
       break
print()
print(f)