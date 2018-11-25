print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.40")
print("create a function partition that spilits the names of soccer players into 2 groups")
num = eval(input("how many names do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till user enter all the words
    sen =input("Enter the names ")
    list.append(sen)
    count = count + 1

    if count == num:
        break
print("The list of names is :-")
print(list) # display the list on the screen
print("\n\n")
print("names of soccer palyer in the first group")
def partition(list):
    for names in list:
        if names[0] >= "A" and names[0] <= "M":
            print(names)

partition(list)
input()
