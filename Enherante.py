class Person:
    def __init__(self, name, gender, age=22):
        self.name = name
        self.age = age
        self.gender = gender
    def say_hi(self):
        print("hello {} from parent class".format(self.name))
class  Student(Person):
    def __init__(self, name, age=22):
         super().__init__(name,age)
    def say_hi(self):
        print("hello {} from student class".format(self.name))
def add_num(x,y):
    return(x+y)
p1 = Person("A", 22)
s1 = Student("B", 15)
s2 = Student("C")
s1.say_hi()
p1.say_hi()

        
        