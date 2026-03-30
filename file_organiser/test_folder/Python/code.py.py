for i in range(3):
    pin = (input("Enter your pin: "))

    if pin == "1234" :
        print("Access Granted!")
        break

    else:
        print("Access Denied!")

else:
    print("CARD BLOCKED!")