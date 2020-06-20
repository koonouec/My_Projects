# Exercise 4(Astrologer's Stars)
m = int(input("how many rows you want to print = "))
n = int(input("Enter 1 or 0 = "))
z = bool(n)
if n==1:
    bool = True
if n == 0:
    bool = False
if z == True:
    for i in range(0,m+1,1):
        print(i*"*")
        i=i+1
if z == False:
    for i in range(m,0,-1):

        print(i*"*")