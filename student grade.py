stu = int(input("Number of students:"))
def grade_avg (x):
    sum2 = 0
    for i in range(1,x+1):
        grade = float(input("Enter student grade:"))
        sum2 +=grade
    avg = sum2/x
    print(avg)

grade_avg(stu)
