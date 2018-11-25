print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.20")
print("for loop that prints the first three characters of each word in the list")
num = eval(input("How many names do you want to enter "))#loop to enter the nmes the number of times user want , in the list
lst=[]
x = 0
while x != num:
    name = input("Enter the name ")
    lst.append(name)
    x = x+1
    if x == num :
        break

print(lst)#print the list

for month in lst: #for loop to extract out the first three elements of each name in list 
    x = month[0]
    y = month[1]
    z = month[2]
    print(x + y + z)

input()
