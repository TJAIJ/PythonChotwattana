num = int(input("Enter your Loop:"))
numtotal = []
for i in range(num):
    data = int(input("Enter Your Data:"))
    numtotal += [data]

numtotal.sort()
print(numtotal)
print(numtotal[0])
lastnum = num-1
print(numtotal[lastnum])