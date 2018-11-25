print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.36")
print("Prints the reverse of the integer ")
import math
num = eval(input("Enter a three digit number "))
def reverse_int(num):
    a = num % 10
    b = num / 10
    b = math.floor(b)
    print(a)
    c = b % 10
    d = b / 10
    print(c)
    d = math.floor(d)
    print(d)

reverse_int(num)
input()
