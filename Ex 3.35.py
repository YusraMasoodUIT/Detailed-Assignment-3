print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.35")
print("calculates the probability ")
n = eval(input("Enter a value for n "))
if n < 0 :
    print("Sorry.. , enter a non negative integer")
else:
    def prob(n):
        a = 2**(-n)
        print(a)
    prob(n)

input()
