print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.21")
print("Program that prints all the even numbers in the list")
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
print("The even numbers are ")
for x in list: #calculates mod of every element in list by dividing it by 2
    modul = x % 2
    if modul == 0 : # if number is even the mod will be zero
        print(x)
input()
