print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.42")
print("create a function function avg() that takes as input a list that contains lists of numbers. Each number list represents the grades a particular student received for a course.")
stu = eval(input("Enter the number of students ")) # ask the user how many students he want to enter
x = 1
stu = stu + 1
list = []
while x != stu :
    print(str(x) + " student")
    subj = eval(input("Enter the number of subjects "))#ask the user about the number of subjects for each student
    y = 0
    list1 = []
    while y != subj:
        marks = eval(input("Enter the marks of the subject "))#ask user to enter the marks of the subjects
        list1.append(marks)#creates a list of marks for each student
        y = y+1
        
        if y == subj:
            break
    list.append(list1)#creates a list which contain seperate list of marks of all subjects
    x = x + 1
    if x == stu:
        break
print(list)#print that list

def avg(list):#start of function to calculate the average of each student
    for stud in list:#seperates the students from each list
        sum1 = 0
        numsubj = 0
        for marks1 in stud:#seperates the marks of each student from the seperatedd student list
            sum1 = sum1 + marks1#adds the marks together
            numsubj = numsubj + 1
        avg = sum1 /numsubj#calculates average
        print(avg)
avg(list)

input()
