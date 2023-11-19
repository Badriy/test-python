sum2 = 0
stu = int(input("Number of stuents:"))
for i in range(1,stu+1):
    grade = float(input("Enter student grade:"))
    sum2 +=grade
avg = sum2/stu
print(avg)