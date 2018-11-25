print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.32")
print("Program that prints the digits of a four digit number")

import math
num = int(input("Enter a four digit numer "))
a = num / 1000
b = num % 1000
a = math.floor(a)
print(a)
c = b /100
d = b %100
c = math.floor(c)
print(c)
e = d / 10
f = d % 10
e = math.floor(e)
print(e)
print(f)

input()
