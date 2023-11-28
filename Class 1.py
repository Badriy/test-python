# class Person:
#     num_of_object =0
#     def __init__(self, name ,age=22):
#         self.__name = name
#         self.__age = age
#         Person.num_of_object +=1
#     def set_name(self,new_name):
#         self .__name = new_name
#     def get_name():
#         print(self.__name)
#     def __str__(self):
#         return"hello {} you are {} years old".format(self.__name,  self.__age)
#     def talk(self):
#         return "{} is talking",format(self.name)
# 
#         
# p1 = Person("Ahmed", 24)
# p2 = Person("Ali", 25)
# p3 = Person("Waleed")
# #print(person1.name)
# #print(person1.age)
# print(p1)
# print(p2)
# print(p2.num_of_object)
# p2.set_name("Ali")
# p2.get_name()
# print(p2)


class Shapes:
    def __init__(self,color, name):
        self.color = color
        self.name = name
    def area(self):
        return "Area of Parent class"
    
    def discription(self):
        print("I am  {} from Shapes class".format(self.name))
        
class Sequare(Shapes):
    def __init__(self, name, color, sid):
        self.sid= sid
        super().__init__(color,name)
        
    def area_(self):
        arear1 = self.sid * self.sid
        return area1
    
class Circle(Shapes):
     def __init__(self, name, color, radius):
         self.radius= radius
         super().__init__(color,name)
     def area(self):
         area2 = 3.14*(self.radius**2)
         return area2
seq = Sequare("green", "Sequare1",3)
cirl = Circle("red","circle1",2)
shap = Shapes("blue","shape")
print(seq.area())
print(cirl.area())
print(shap.area())
seq.discription()
         
         
         
        
