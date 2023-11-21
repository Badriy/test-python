#writ a function that return the are of ruglar polygon using header area(n , side), writ function that promot user to enter the number
#of side of a regular polygon an display it area
#Enter the number of ides:5
#Enter the side:6.5
#The area of polygon is 72.69017
import math
n = int(input("Enter  number of sides: "))
s = float(input("Enter the side: "))

def polygon_area (n,s):
    area = ((n*s**2) / (4*math.tan(math.pi/n)))
    return (area)
print (polygon_area(n,s))
print (round(polygon_area(n,s),2))