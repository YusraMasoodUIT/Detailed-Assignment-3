print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.25")
print("Program that requests a list of student names from the user and prints those names that start with letters A through M.")


num = eval(input("how many numbers do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till the user enters all the words
    sen =input("Enter the name ")
    list.append(sen)
    count = count + 1

    if count == num:
        break
print("The list of names is :-")
print(list) # display the list on the screen
print("\n\n")
print("names that start with the letters in between A and M are")
for names in list:
    if names[0] >= "A" and names[0] <= "M"  :
        print(names)

input()
