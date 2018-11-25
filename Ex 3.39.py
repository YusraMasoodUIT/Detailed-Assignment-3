print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.39")
print("create a function collision() to see if two balls collide or not")
import math
x1 = eval(input("Enter the x cordinate for centre of the first ball "))
y1 = eval(input("Enter the y cordinate for centre of the first ball "))
r1 = eval(input("Enter the radius for the first ball "))
x2 = eval(input("Enter the x cordinate for centre of the second ball "))
y2 = eval(input("Enter the y cordinate for centre of the second ball "))
r2 = eval(input("Enter the radius for the second ball "))
def collision(x1 , y1 ,r1 , x2 , y2 ,r2):
    x= x2 - x1
    y = y2 - y1
    dist = ((x**2) + (y**2))
    totaldist = math.sqrt(dist)
    rad = 2 * r1 #we'll be assuming that both balls are of same size i.e. the radius of both balls are same
    if totaldist < rad:
        return True
    else:
        return False


input()
