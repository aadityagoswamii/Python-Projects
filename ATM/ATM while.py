attempts = 0

while attempts < 3:
    pin = input("Enter your pin: ")

    if pin == "1234":
        print("Access Granted!")
        break
    else:
        print("Access Denied!")
        attempts += 1

if attempts == 3:
    print("Card Blocked")