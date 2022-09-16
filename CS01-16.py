from re import X


x = 0
a = 0

while a >= 0 :
    a = float(input("Input Number : "))
    if a <= -1 :
        break
    else:
        x += a
    print(x)
print("Break")