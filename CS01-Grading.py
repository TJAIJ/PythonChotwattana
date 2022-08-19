db = 0
while db == 0:
    sc1 = int(input("KananKep1 : "))

    if sc1 >= 0 and sc1 <= 30 :
        print("KananKep1 : ",sc1)
        db = 1
    else:
        print("Error")
        db = 0

db = 0

while db == 0:
    sc2 = int(input("KananSorpKlangPark2 : "))

    if sc2 >= 0 and sc2 <= 30 :
        print("KananSorpKlangPark2 : ",sc2)
        db = 1
    else:
        print("Error")
        db = 0
db = 0
while db == 0:
    sc3 = int(input("KananSorpPrayPark3 : "))

    if sc3 >= 0 and sc3 <= 40 :
        print("KananSorpPrayPark3 : ",sc3)
        db = 1
    else:
        print("Error")
        db = 0

sum = sc1+sc2+sc3

if sum <=49 :
    print(" F ")
elif sum <= 54:
    print(" D ")
elif sum <= 59:
    print(" D+ ")
elif sum <= 64:
    print(" C ")
elif sum <= 69:
    print(" C+ ")
elif sum <= 74:
    print(" B ")
elif sum <= 79:
    print(" B+ ")
elif sum <= 100:
    print(" A ")
print("Score = ",sum)