menu = {"maramari": 90,
        "rasmalai": 100,
        "thabadi": 150,
        "rajawadi": 160,
        "sizzler": 149,
        "badam shake": 65,
        "gulabmasti": 50,
        "kaju katri": 280,
        "coco": 80}

cart = []
total = 0

print("______Fresh Dairy______")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("________________________")

while True:
 food = input("select item(q to quit):").lower()

 if food == "q":
     break

 elif menu.get(food) is not None:
     cart.append(food)

     print(cart)


for food in cart:
    total += menu.get(food)
    print(food, end=" ")

    print()
    print(f"total is ${total:.2f}")
