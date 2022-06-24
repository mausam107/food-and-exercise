def getdate():
    import datetime
    return datetime.datetime.now()

def store_data(name):

    c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

    if (c == 1):

        path=name+'_food_data'+'.txt'

        value = input("\nEnter name of food = ")

        with open(path,"a") as f:

            # f.write(str([str(getdate())])+": "+value+"\n")

            f.write("["+str(getdate())+"]:")
            f.write(value)
            f.write("\n")


            print("\nSuccessfully added\n")

    elif c == 2:

        path=name+'_exercise_data'+'.txt'

        value = input("\nEnter name of exercise = ")

        with open(path,"a") as f:

            f.write(str([str(getdate())])+": "+value+"\n")

        print("Successfully added\n")

    else:

            print("wrong entry")

def show_data(name):

    c = int(input("\nFor food , press 1\nFor exercise , press 2\n"))

    if c==1:
        path=name+'_food_data'+'.txt'
        with open(path) as f:
            content=f.read()
            print(content)

    elif c==2:
        path=name+'_exercise_data'+'.txt'
        with open(path) as f:
            content=f.read()
            print(content)

    else:
        print("Wrong choice")
    



print("\n**** Health Management System ****")

a = int(input("\nPress 1 : To Store data\nPress 2 : To Show data\n"))
name=input('Enter your name')

if a == 1:

    store_data(name)

elif a == 2:
    
    show_data(name)