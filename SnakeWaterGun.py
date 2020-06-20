'''Snake Water Game'''
import random
print("Hello, It's a Stone Paper Scissor game\n")
j =0
while (j<100):
    print("Would you like to play ?\n")
    print("Press 1 to Play or Press 0 to Exit ")
    Play_check = int(input())
    if Play_check == 1:
        count_computer=0
        count_User=0
        points = 0
        i = 0
        while(i<10):
            option_1, option_2, option_3 = "Stone", "Paper", "Scissor"
            print(option_1, option_2, option_3)
            print("Choose one from above Elements and Write Proper spells as shown above Because its case sensitive ")
            Element = input("Your choice = ")
            Computer_Choice = ["Stone", "Paper", "Scissor"]
            computer = random.choice(Computer_Choice)
            print("Computer choice = ", computer)
            if (computer == "Stone" and Element =="Stone" or computer == "Paper" and Element =="Paper" or computer == "Scissor" and Element =="Scissor"):
                print("Draw")
                print("Computer Score : ", count_computer) 
                print("Your score : ", count_User)
                i+=1
            elif (computer == "Stone" and Element =="Paper"):
                print("You Won")
                print("Computer Score : ", count_computer) 
                print("Your score : ", count_User+1)
                count_User+=1
                i+=1
            elif (computer == "Stone" and Element =="Scissor"):
                print("You Lost")
                print("Computer Score : ", count_computer+1) 
                print("Your score : ", count_User)
                count_computer+=1
                i+=1
            elif (computer == "Paper" and Element =="Stone"):
                print("You Lost")
                print("Computer Score : ", count_computer+1) 
                print("Your score : ", count_User)
                count_computer+=1
                i+=1
            elif (computer == "Paper" and Element =="Scissor"):
                print("You Won")
                print("Computer Score : ", count_computer) 
                print("Your score : ", count_User+1)
                count_User+=1
                i+=1
            elif (computer == "Scissor" and Element =="Stone"):
                print("You Won")
                print("Computer Score : ", count_computer) 
                print("Your score : ", count_User+1)
                count_User+=1
                i+=1
            elif (computer == "Scissor" and Element =="Paper"):
                print("You Lost")
                print("Computer Score : ", count_computer+1) 
                print("Your score : ", count_User)
                count_computer+=1
                i+=1
            else:
                print("wrong input")
                i+=1
        print("Your Total Score : ", count_User)
        print("Computer Score : ", count_computer)
        if (count_User>count_computer):
            print("Congratulation, You won")
        elif(count_User<count_computer):
            print("You Lost this game")
        elif(count_User == count_computer):
            print("Game Draw")
    if Play_check == 0:
        break


                
