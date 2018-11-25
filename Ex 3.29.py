print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.29")
print("Program that requests a positive integer n and prints on the screen all the positive divisors of n")
num = eval(input("Enter a number "))
for divisor in range(1 , num + 1):
    x = num % divisor
    if x == 0:
        print(divisor)
input()
