from random import randint
n = randint(1,10)


while(True):
    gus_n=int(input("enter number:"))
    if (gus_n > n):
        print ("Go down")
        continue
    elif (gus_n < n):
        print("Go up")
        continue
    else:
        print("correct number")
    break    
    
