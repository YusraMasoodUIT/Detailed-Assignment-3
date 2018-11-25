print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.24")
print("Program that ask user for a list of words and print each word which is not 'secret'")

num = eval(input("how many words do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till the user enters all the words
    sen =input("Enter the word ")
    list.append(sen)
    count = count + 1

    if count == num:
        break
print("The list of words is :-")
print(list) # display the list on the screen
print("\n")
for words in list:#beginning of for loop to extract out the words 
    if words != 'secret' :#check if the word is 'secret'
        print(words)#print if it is not

input()
