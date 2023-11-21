list_ = [8, 11 , 5 ,4]
for i in range(len(list_)):
    print(list_[i])
print('---------------')
for i in [2,4]:
    print(i)
print('---------------')

s= [2,5,5,1,7]
x=list (s)
print(x)
x[4] = 5
print(x)
print(s)


print('---------------')

s= [2,5,5,1,7]
x= s.copy()
print(x)
x[4] = 5
print(x)
print(s)
