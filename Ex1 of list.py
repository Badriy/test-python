# write for loop itrati
#EX1 :A.print lement without comma
s = [2,5,5,1,7]
for i in s:
    print(i, end = " ")
    
print()
#EX1 :B.print list*2    
s = [2,5,5,1,7]
for i in s:
    print(i*2, end = " ")
    
print()
#EX1 :C.count negative number
count=0    
s = [-2,5,5,-1,7]
for i in s:
    if (i < 0):
         count +=1
print(count)

print()
# append command
ls = []
ls.append("badriya")
# insrt command
ls.insert(1,"amal")
print(ls)
print()
# pop function
s = [-2,5,5,-1,7]
s.insert(1,9)
print(s)
s.append(9)
print(s)
# remove function
s.remove(5)
print(s)
s.pop(-1)
s.pop()
print(s)

print ()

#replication
ls=[0,0,0,0]
ls=[0]*4
print(ls)

print()

