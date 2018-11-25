print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.26")
print("Program that requests a nonempty list from the user and prints on the screen a message giving the first and last element of the list")
num = eval(input("how many name do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till user enter all the words
    sen =input("Enter the name ")
    list.append(sen)
    count = count + 1

    if count == num:
        break
print("The list of names is :-")
print(list) # display the list on the screen
print("\n\n")
print("The first element of your list is :-  ")
print(list[0])
print("The last element of your list is :-  ")
print(list[-1])

input()
