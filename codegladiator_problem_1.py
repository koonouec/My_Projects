''' The Powerpuff Girls '''
def main():
    try:
        N = int(input())
        list_1= [int(i) for i in input().split()][:N]
        list_2= [int(i) for i in input().split()][:N]
    except Exception as e:
        e
    powerpuff_made = 0
    while True:
        n = list(map(lambda n,m : n-m, list_2, list_1))
        powerpuff_made+=1
        if 0 in n:
            print(powerpuff_made)
            break
        elif 0 not in n:
            list_2.clear()
            for k in range(len(n)):
                list_2.append(n[k])
main()



