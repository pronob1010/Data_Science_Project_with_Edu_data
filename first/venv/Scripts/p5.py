while 1:
    car_menu = input("Enter the key :")
    if car_menu == "HELP" or car_menu == "help":
        print("start")
        print("slow")
        print("stop")

    elif car_menu == "start":
        print("Let's Go")
    elif car_menu == "slow":
        print("Ok. Boss!")
    elif car_menu == "stop":
        print('What was the drive ?')
        break
    else:
        print("I dont understand")
