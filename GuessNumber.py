''' Guess The Number '''
def GuessNumber():
    Number = 89
    print("Hello Sir i Have a number hidden in my pocket. Can u Guess this Number ?")
    print("Press y to play or n to close this game")
    x =input()
    if(x=="y"):
        print("Lets Play")
        print("You have 7 attempts to guess this number ")
        attempts=1
        Gu = 1
        while(Gu<8 and attempts<8):
            m = int(input("Enter ur guess = "))
            if m>Number:
                print("Nope, guess smaller friend ")
                print("You have", 7-attempts, "attempts left")
                Gu+=1
                attempts+=1
            if m<Number:
                print("Nope, Guess greater friend")
                print("You have", 7-attempts, "attempts left")
                Gu+=1
                attempts+=1
            if m == Number:
                print("Congrats You won! the number is ", Number)
                print("You took ", Gu, " attempts")
                print("Well Played Sir")
                break
            if(attempts>7):
                print("Sorry Sir you have 0 attempts left! Game Over! The number is = ", Number)
                print("Well Played Sir")
    if (x  == "n"):
        print("Thank you have a nice day")
GuessNumber()