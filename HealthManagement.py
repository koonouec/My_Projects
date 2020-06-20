''' Health Management System '''
def getdate():
    import datetime
    return datetime.datetime.now()
getdate()
CLient_1, CLient_2, CLient_3 = "Harry", "Rahul" , "Hammad"
print("Hello")
print("Enter CLient name YOu want to access")
print(CLient_1, CLient_2, CLient_3)
print("Press 1 for Harry\nPress 2 for Rahul\nPress 3 for Hammad")
client_name=int(input())
if client_name == 1:
    def Harry():
        print("Hi Harry")
        Diet_H, Exercise_H ="Diet", "Workout"
        j = 0
        while(j<1000):
            print(Diet_H, Exercise_H)
            print("Press 1 to Lock and Retrieve Diet\nPress 2 to Lock and Retrieve Workout\nPress 0 to exit")
            options_H =int(input())
            if options_H == 1:
                print("Press 1 to Lock Diet\nPress 2 to Retrieve Diet\nPress 3 to delete Previous Diet\nPress 4 to Exit")
                option_check = int(input())
                if option_check == 1:
                    try:
                        with open("D:\My_Work\Diet.txt", "x") as f:
                            print("Enter Your Diet")
                            food = input()
                            f.write("\n--------\n")
                            f.write("New Diet\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                            f.write("\n--------\n")
                            print("We have locked ur diet Harry")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more items in your diet")  
                                print("Press 1 to add more items or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update Items")
                                    update_food = input()
                                    f.write("\n--------\n")
                                    f.write("New Diet\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                    f.write("\nItems Updated")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break
                    except Exception as e:
                        e
                        with open("D:\My_Work\Diet.txt", "a") as f:
                            print("Enter Your Diet")
                            food = input()
                            f.write("\n--------\n")
                            f.write("New Diet\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                            f.write("\n--------\n")
                            print("We have locked ur diet Harry")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more items in your diet")  
                                print("Press 1 to add more items or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update Items")
                                    update_food = input()
                                    f.write("\n--------\n")
                                    f.write("New Diet\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                    f.write("\nItems Updated")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break  
                elif option_check == 2:
                    with open("D:\My_Work\Diet.txt", "r") as f:
                        print(f.read()) 
                elif option_check == 3:
                    with open("D:\My_Work\Diet.txt", "w") as f:
                        f.write("    ")
                elif option_check == 4:  
                    break 
                else:
                    print("Wrong Input")
            if options_H == 2:
                print("Press 1 to Lock workout\nPress 2 to Retrieve workout\nPress 3 to delete Previous workout\nPress 4 to Exit")
                option_check = int(input())
                if option_check == 1:
                    try:
                        with open("D:\My_Work\workout.txt", "x") as f:
                            print("Enter Your workout")
                            workout = input()
                            f.write("\n--------\n")
                            f.write("New workout\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                            f.write("\n--------\n")
                            print("We have locked ur workout Harry")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more in your workout")  
                                print("Press 1 to add more or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update")
                                    update_workout = input()
                                    f.write("\n--------\n")
                                    f.write("New workout\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                    f.write("\nUpdated")
                                    print("Updated succesfully")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break
                    except Exception as e:
                        e
                        with open("D:\My_Work\workout.txt", "a") as f:
                            print("Enter Your workout")
                            workout = input()
                            f.write("\n--------\n")
                            f.write("New workout\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                            f.write("\n--------\n")
                            print("We have locked ur workout Harry")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more in your workout")  
                                print("Press 1 to add more or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update")
                                    update_workout = input()
                                    f.write("\n--------\n")
                                    f.write("New workout\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                    f.write("\nUpdated")
                                    print("Updated succesfully")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break  
                elif option_check == 2:
                    with open("D:\My_Work\workout.txt", "r") as f:
                        print(f.read()) 
                elif option_check == 3:
                    with open("D:\My_Work\workout.txt", "w") as f:
                        f.write("    ")
                elif option_check == 4:  
                    break 
                else:
                    print("Wrong Input")
            elif options_H == 0:
                break         
    Harry()
if client_name == 2:
    def Rahul():
        print("Hi Rahul")
        Diet_H, Exercise_H ="Diet", "Workout"
        j = 0
        while(j<1000):
            print(Diet_H, Exercise_H)
            print("Press 1 to Lock and Retrieve Diet\nPress 2 to Lock and Retrieve Workout\nPress 0 to exit")
            options_H =int(input())
            if options_H == 1:
                print("Press 1 to Lock Diet\nPress 2 to Retrieve Diet\nPress 3 to delete Previous Diet\nPress 4 to Exit")
                option_check = int(input())
                if option_check == 1:
                    try:
                        with open("D:\My_Work\Diet.txt", "x") as f:
                            print("Enter Your Diet")
                            food = input()
                            f.write("\n--------\n")
                            f.write("New Diet\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                            f.write("\n--------\n")
                            print("We have locked ur diet Rahul")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more items in your diet")  
                                print("Press 1 to add more items or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update Items")
                                    update_food = input()
                                    f.write("\n--------\n")
                                    f.write("New Diet\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                    f.write("\nItems Updated")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break
                    except Exception as e:
                        e
                        with open("D:\My_Work\Diet.txt", "a") as f:
                            print("Enter Your Diet")
                            food = input()
                            f.write("\n--------\n")
                            f.write("New Diet\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                            f.write("\n--------\n")
                            print("We have locked ur diet Rahul")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more items in your diet")  
                                print("Press 1 to add more items or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update Items")
                                    update_food = input()
                                    f.write("\n--------\n")
                                    f.write("New Diet\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                    f.write("\nItems Updated")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break  
                elif option_check == 2:
                    with open("D:\My_Work\Diet.txt", "r") as f:
                        print(f.read()) 
                elif option_check == 3:
                    with open("D:\My_Work\Diet.txt", "w") as f:
                        f.write("    ")
                elif option_check == 4:  
                    break 
                else:
                    print("Wrong Input")
            if options_H == 2:
                print("Press 1 to Lock workout\nPress 2 to Retrieve workout\nPress 3 to delete Previous workout\nPress 4 to Exit")
                option_check = int(input())
                if option_check == 1:
                    try:
                        with open("D:\My_Work\workout.txt", "x") as f:
                            print("Enter Your workout")
                            workout = input()
                            f.write("\n--------\n")
                            f.write("New workout\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                            f.write("\n--------\n")
                            print("We have locked ur workout Rahul")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more in your workout")  
                                print("Press 1 to add more or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update")
                                    update_workout = input()
                                    f.write("\n--------\n")
                                    f.write("New workout\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                    f.write("\nUpdated")
                                    print("Updated succesfully")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break
                    except Exception as e:
                        e
                        with open("D:\My_Work\workout.txt", "a") as f:
                            print("Enter Your workout")
                            workout = input()
                            f.write("\n--------\n")
                            f.write("New workout\n")
                            f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                            f.write("\n--------\n")
                            print("We have locked ur workout Rahul")
                            i = 0
                            while(i<1000):
                                print("Would you like to add more in your workout")  
                                print("Press 1 to add more or Press 0 to Exit")
                                open_add = int(input())
                                if open_add == 1:
                                    print("Update")
                                    update_workout = input()
                                    f.write("\n--------\n")
                                    f.write("New workout\n")
                                    f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                    f.write("\nUpdated")
                                    print("Updated succesfully")
                                    f.write("\n--------\n")
                                    i+=1        
                                elif open_add == 0:
                                    break  
                elif option_check == 2:
                    with open("D:\My_Work\workout.txt", "r") as f:
                        print(f.read()) 
                elif option_check == 3:
                    with open("D:\My_Work\workout.txt", "w") as f:
                        f.write("    ")
                elif option_check == 4:  
                    break 
                else:
                    print("Wrong Input")
            elif options_H == 0:
                break 
    
    Rahul()
if client_name == 3:
    print("Hi Hammad")
    Diet_H, Exercise_H ="Diet", "Workout"
    j = 0
    while(j<1000):
        print(Diet_H, Exercise_H)
        print("Press 1 to Lock and Retrieve Diet\nPress 2 to Lock and Retrieve Workout\nPress 0 to exit")
        options_H =int(input())
        if options_H == 1:
            print("Press 1 to Lock Diet\nPress 2 to Retrieve Diet\nPress 3 to delete Previous Diet\nPress 4 to Exit")
            option_check = int(input())
            if option_check == 1:
                try:
                    with open("D:\My_Work\Diet.txt", "x") as f:
                        print("Enter Your Diet")
                        food = input()
                        f.write("\n--------\n")
                        f.write("New Diet\n")
                        f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                        f.write("\n--------\n")
                        print("We have locked ur diet Hammad")
                        i = 0
                        while(i<1000):
                            print("Would you like to add more items in your diet")  
                            print("Press 1 to add more items or Press 0 to Exit")
                            open_add = int(input())
                            if open_add == 1:
                                print("Update Items")
                                update_food = input()
                                f.write("\n--------\n")
                                f.write("New Diet\n")
                                f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                f.write("\nItems Updated")
                                f.write("\n--------\n")
                                i+=1        
                            elif open_add == 0:
                                break
                except Exception as e:
                    e
                    with open("D:\My_Work\Diet.txt", "a") as f:
                        print("Enter Your Diet")
                        food = input()
                        f.write("\n--------\n")
                        f.write("New Diet\n")
                        f.write("Date and time = "+str(getdate()) + "\n" + "Your Diet = "+ food)
                        f.write("\n--------\n")
                        print("We have locked ur diet Hammad")
                        i = 0
                        while(i<1000):
                            print("Would you like to add more items in your diet")  
                            print("Press 1 to add more items or Press 0 to Exit")
                            open_add = int(input())
                            if open_add == 1:
                                print("Update Items")
                                update_food = input()
                                f.write("\n--------\n")
                                f.write("New Diet\n")
                                f.write("Date and time = "+str(getdate()) + "\n" + "Updated Items = "+ update_food)
                                f.write("\nItems Updated")
                                f.write("\n--------\n")
                                i+=1        
                            elif open_add == 0:
                                break  
            elif option_check == 2:
                with open("D:\My_Work\Diet.txt", "r") as f:
                    print(f.read()) 
            elif option_check == 3:
                with open("D:\My_Work\Diet.txt", "w") as f:
                    f.write("    ")
            elif option_check == 4:  
                break 
            else:
                print("Wrong Input")
        if options_H == 2:
            print("Press 1 to Lock workout\nPress 2 to Retrieve workout\nPress 3 to delete Previous workout\nPress 4 to Exit")
            option_check = int(input())
            if option_check == 1:
                try:
                    with open("D:\My_Work\workout.txt", "x") as f:
                        print("Enter Your workout")
                        workout = input()
                        f.write("\n--------\n")
                        f.write("New workout\n")
                        f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                        f.write("\n--------\n")
                        print("We have locked ur workout Hammad")
                        i = 0
                        while(i<1000):
                            print("Would you like to add more in your workout")  
                            print("Press 1 to add more or Press 0 to Exit")
                            open_add = int(input())
                            if open_add == 1:
                                print("Update")
                                update_workout = input()
                                f.write("\n--------\n")
                                f.write("New workout\n")
                                f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                f.write("\nUpdated")
                                print("Updated succesfully")
                                f.write("\n--------\n")
                                i+=1        
                            elif open_add == 0:
                                break
                except Exception as e:
                    e
                    with open("D:\My_Work\workout.txt", "a") as f:
                        print("Enter Your workout")
                        workout = input()
                        f.write("\n--------\n")
                        f.write("New workout\n")
                        f.write("Date and time = "+str(getdate()) + "\n" + "Your workout = "+ workout)
                        f.write("\n--------\n")
                        print("We have locked ur workout Hammad")
                        i = 0
                        while(i<1000):
                            print("Would you like to add more in your workout")  
                            print("Press 1 to add more or Press 0 to Exit")
                            open_add = int(input())
                            if open_add == 1:
                                print("Update")
                                update_workout = input()
                                f.write("\n--------\n")
                                f.write("New workout\n")
                                f.write("Date and time = "+str(getdate()) + "\n" + "Updated = "+ update_workout)
                                f.write("\nUpdated")
                                print("Updated succesfully")
                                f.write("\n--------\n")
                                i+=1        
                            elif open_add == 0:
                                break  
            elif option_check == 2:
                with open("D:\My_Work\workout.txt", "r") as f:
                    print(f.read()) 
            elif option_check == 3:
                with open("D:\My_Work\workout.txt", "w") as f:
                    f.write("    ")
            elif option_check == 4:  
                break 
            else:
                print("Wrong Input")
        elif options_H == 0:
            break 