print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.37")
print("calculates the slope and the distance of two points ")
import math
x1 = eval(input("Enter the x cordinate of the first point "))
y1 = eval(input("Enter the y cordinate of the first point "))
x2 = eval(input("Enter the x cordinate of the second point "))
y2 = eval(input("Enter the y cordinate of the second point "))
def points(x1 , y1 , x2 ,y2):
    x = x2 - x1
    if x == 0 :
        slope = "infinity"
    else:
        y = y2 - y1
        slope = y /x
    y = y2 - y1
    distx = x**2
    disty = y**2
    dist = distx + disty
    totaldist = math.sqrt(dist)
    print("The slope is " +str(slope) + " and the distance is " +str(totaldist))

points(x1 , y1 , x2 ,y2)
input()
