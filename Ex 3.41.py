print("Yusra Masood , 18B-093-CS ,Section A")
print("Ex 3.41")
print("create a function function lastF() that takes as input two strings of the form 'FirstName' and 'LastName', respectively, and returns a string of the form 'LastName, F")
fname = input("Enter your first name ")
lname = input("Enter your last name ")
def lastF(fname , lname):
    x = fname[0]
    print(lname+ ", " + x)

lastF(fname ,lname)

input()
