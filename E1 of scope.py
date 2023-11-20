#write a function that computes the sum of the digit in an integr.use sum_digit(234) returns 9 (2+3+4).write a test program tha
#promots the user to enter an inteager and display he um of all digits
n = int(input("Enter number :"))
def sum_digit(a):
    sum_= 0
    i = n
    while (i!=0):
      sum_+=int(i)%10
      i= int(i)//10
    return sum_
    
r=sum_digit(n)
print(r)