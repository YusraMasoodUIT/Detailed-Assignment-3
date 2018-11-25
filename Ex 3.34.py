print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.34")
print("Function that calculates pay ")
wage = eval(input("Enter your hourly wage "))
hours = eval(input("Enter the number of hours you have worked "))
def pay(wage , hours):
    if hours > 40:
        x = hours - 40
        wage1 = wage * 1.5
        extrapay = wage1 * x
        normpay = wage * 40
        totalpay = extrapay + normpay
        print("Your total pay is " + str(totalpay))
    else:
        y = wage * hours
        print("Your total pay is " +str(y))

pay(wage , hours)
input()
