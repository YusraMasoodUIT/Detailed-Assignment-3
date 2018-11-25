print("Yusra Masood , 18B -093 -CS , Section A")
print("Ex 3.44")
print("Calculate the distance of lightning strike")
time = eval(input("Enetr the time elapsed "))
def distance(time):
    dist = 340.29 * time
    distkm = dist / 1000
    print(str(distkm)+"km")

distance(time)
input()
