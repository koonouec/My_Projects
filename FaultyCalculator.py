''' Faulty Calculator '''

def Faulty_Calculator():
    my_operators = "+ , -, *, /"
    print("Avaialable Operators are :" + my_operators)
    op = input("Enter Operator you want to use = ")
    n = int(input("Enter First Number = "))
    m = int(input("Enter Second Numer = "))
    if op == "+":
        if(n==45 and m==3):
            solution = 77
        else:
            solution = n + m
        print(solution)
    if op == "*":
        if(n==45 and m==3):
            solution = 555
        else:
            solution = n * m
        print(solution)
    if op == "/":
        if(n==56 and m==6):
            solution = 4
        else:
            solution = n / m
        print(solution)
    if op == "-":
        if(n==77 and m==6):
            solution = 21
        else:
            solution = n - m
        print(solution) 
Faulty_Calculator()