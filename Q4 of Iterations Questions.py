#Q4 of Iterations Questions:
#Check whether a number is a Narcissistic number or not in Python,
#if you know that Narcissistic numbers are the special type of
#numbers where that number can be formed by sum of its own
#digits raised to the power of no. of digits.
#Example output:
#153
#Yes

num=input()
m=int(num)
d=0
q=m
while(m!=0):
     p=m%10
     d+=p**(len(num))
     m=m//10
if(d==q):
    print('Yes')
else:
    print('No')