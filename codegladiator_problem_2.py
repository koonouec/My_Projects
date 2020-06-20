''' Beyblade World Championship '''
def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        power_G_Revolution = [int(i) for i in input().split()]
        power_Opponent_members = [int(i) for i in input().split()]
        power_G_Revolution.sort()
        # print(power_G_Revolution)
        # print(sorted(power_G_Revolution))
        # print(power_Opponent_members)
        for pow_O in power_Opponent_members:
            for pow_G in power_G_Revolution:
                if pow_G > pow_O:
                    power_G_Revolution.remove(pow_G)
                    break
        print(str(N - len(power_G_Revolution)))
main()