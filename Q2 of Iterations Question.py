#Q2 of Iterations Questions:
#Print all perfect number from 1 to 100, if you know that a perfect
#number is a positive integer that is equal to the sum of its
#positive divisors, excluding the number itself. For instance, 6 has
#divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a
#perfect number.

number = int(input("Enter  th number:"))
positive_divisior = input("Enter positive divisior number:")

list = []
for i in positive_divisior.spilt(","):
    list.append(int(i))
    perfect_number= sum(list)
    
if (list == number):
    print(perfect_number, "This number is perfect")