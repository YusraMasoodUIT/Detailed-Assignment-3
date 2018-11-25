print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.31")
print("Program that calculates if the dart thrown hit the board or not")
import math
x = eval(input("Enter the x co-ordinate "))
y = eval(input("Enter the y co-ordinate "))
sum1 = ((x**2)+ (y**2))
total = math.sqrt(sum1)
if total < 8:
    print("It is in")
    
input()
