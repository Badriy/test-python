counter=0
a = ("0123456789")
x = input("Enter a text:")
for chr1 in x:
    if (chr1 in a):
        counter +=1
print(counter)    