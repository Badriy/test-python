#count the area of three shapes:
#Traingle area = A = 1/2 *b * h

b=int(input("Enter the base of the traingle:"))
h=int(input("Enter th high of the traingle:"))


def traingle_area(b,h):
    traingle=(b * h)/2
    return(traingle)

#Square area = Area = side**2
side=int(input("Enter the side of the squar:")) 
def square_area(side**2):
    square= side**2
    return(square)
#Circle area =  A = π r² 
def circle_area(PI,r1,h2):
    circle_area=(2 * PI * 1) + 2*PI (r**2)
    return(circle_area)
#cylinder area=(2π r h+2π r2)
def cylinder area(PI,r1,h2):
    cylinder=((2 * PI *r1) + 2*PI(r1**2))
     return(cylinder area)
    
 while 1 :
    chocie=input("enter 1,2,3,4,5(for quiting): ")
    if(choose==1):
          b=int(input("enter height :"))
          h=int(input("enter base :"))
          result =trainagle_shape(b,h)
          print("The area of traingle is : "+str(result))
    elif(choose==2):
          b=int(input("enter height :"))
          h=int(input("enter base :"))
          result =sequare_shape(b,h)
          print("The area of traingle is : "+str(result))
    elif(choose==3):
          n=int(input("enter the radius : "))
          result= circle_shape(n)
          print("The area of circle: "+str(result))
    elif(choose==4):
        n=int(input("enter radius : "))
           