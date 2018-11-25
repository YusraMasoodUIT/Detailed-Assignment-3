print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.43")
print("Function hit which calculates if the dart hit the board")
import math
xC = eval(input("Enter the x co-ordinate of the centre of the circle ")) #ask for the x and y co-ordinate of the centre of the circle
yC = eval(input("Enter the y co-ordinate of the centre of the circle "))
r = eval(input("Enter the radius of the circle ")) #ask for the radius of the circle
xP = eval(input("Enter the x co-ordinate of the point "))#ask for the co-ordinates of the point where the dart hit
yP = eval(input("Enter the y co-ordinate of the point "))
def hit(xC , yC , r , xP ,yP): #function which calculates if the dart hit the board or not
    x = xP - xC
    y = yP - yC
    sum1 = ((x**2)+ (y**2))
    total = math.sqrt(sum1)
    if total <= r:
        return True
    else:
        return False
input()
