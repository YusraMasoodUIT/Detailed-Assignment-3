print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.22")
print("Program that prints prints the numbers in the list whose square is divisible by 8")
num = eval(input("how many numbers do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till user enter all the numbers
    lsint = eval(input("Enter the number "))
    list.append(lsint)
    count = count + 1

    if count == num:
        break
print("The list of integers is :-")
print(list) # display the list on the screen
print("\n")
print("The numbers whoose square is divisible by 8 are :- ")
for x in list: #calculates if the square of the number is divisible by 8
    y = x**2
    modul = y % 8
    if modul == 0 : # if number is even the mod will be zero
        print(x)


input()
