#Q5 of iteration question:

#Print all perfect number from 1 to 100, if you know that a perfect
#number is a positive integer that is equal to the sum of its
#positive divisors, excluding the number itself. For instance, 6 has
#divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a
#perfect number.


for n in range (1,101):
    divi = []
    for j in range(1,n):
        if n%j == 0:
           divi.append(j)
    sum_ = sum(divi)
    if(n == sum_):
       print(n)
