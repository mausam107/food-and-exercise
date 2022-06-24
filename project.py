def getdate():
    import datetime
    return datetime.datetime.now()

def store_data(inp1):

    """This is to store the data"""

    if inp1 == 1:     #This inp1 here is for "store data"

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if (c == 1):

            value = input("\nEnter name of food = ")

            with open("Mausam_Food_data.txt","a") as f:

                # f.write(str([str(getdate())])+": "+value+"\n")

                f.write("["+str(getdate())+"]:")
                f.write(value)
                f.write("\n")


                print("\nSuccessfully added\n")

        elif c == 2:

            value = input("\nEnter name of exercise = ")

            with open("Mausam_exercise_data.txt","a") as f:

                f.write(str([str(getdate())])+": "+value+"\n")

            print("Successfully added\n")

        else:

            print("wrong entry")

    elif inp1 == 2:

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if (c == 1):

            value = input("\nEnter name of food = ")

            with open("Ayush_Food_data.txt","a") as f:

                f.write(str([str(getdate())])+": "+value+"\n")

                print("Successfully added\n")

        elif c == 2:

            value = input("\nEnter name of exercise = ")

            with open("Ayush_exercise_data.txt","a") as f:

                f.write(str([str(getdate())])+": "+value+"\n")

            print("Successfully added\n")

        else:

            print("wrong entry")

    elif inp1 == 3:

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if c == 1:

            value = input("\nEnter name of food = ")

            with open("Versha_Food_data.txt","a") as f:

                f.write(str([str(getdate())])+": "+value+"\n")

                print("Successfully added\n")

        elif c == 2:

            value = input("\nEnter name of exercise = ")

            with open("Versha_exercise_data.txt","a") as f:

                f.write(str([str(getdate())])+": "+value+"\n")

            print("Successfully added\n")

        else:

            print("wrong entry")

    else:

        print("Wrong entry")


def show_data(inp2):

    """"This is to show data"""

    if inp2 == 1:

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if c == 1:

            with open("Mausam_Food_data.txt") as f:

                for i in f:

                    print(i)

        elif c == 2:

            with open("Mausam_exercise_data.txt") as f:

                for i in f:

                    print(i)

        else:

            print("Wrong choice")

    elif inp2 == 2:

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if c == 1:

            with open("Ayush_Food_data.txt") as f:

                for i in f:

                    print(i)

        elif c == 2:

            with open("Ayush_exercise_data.txt") as f:

                for i in f:

                    print(i)

        else:

            print("Wrong choice")

    elif inp2 == 3:

        c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

        if c == 1:

            with open("Versha_Food_data.txt") as f:

                for i in f:

                    print(i)

        elif c == 2:

            with open("Versha_exercise_data.txt") as f:

                for i in f:

                    print(i)

        else:

            print("Wrong choice")


print("\n**** Health Management System ****")

a = int(input("\nPress 1 : To Store data\nPress 2 : To Show data\n"))

if a == 1:

    inp1 = int(input("\nPress 1 : For Mausam\nPress 2 : For Ayush\nPress 3 : For Versha\n"))

    store_data(inp1)

elif a == 2:

    inp2 = int(input("\nPress 1 : For Mausam\nPress 2 : For Ayush\nPress 3 : For Versha\n"))
    show_data(inp2)
