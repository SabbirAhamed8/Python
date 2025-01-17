#concession stand program

menu = {
    "hotdog": 2.00,
    "hamburger": 3.00,
    "fries": 1.00,
    "soda": 1.50
}

cart = []
total = 0

print("------Menu------")

for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("Enter items (q for quit): ")

while True:
    item = input().lower().strip()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total += menu[item]
    

print("------Your cart------")

for item in cart:
      print(f"{item:10} : ${menu[item]:.2f}")

print("--------------------------")
print(f"Total{': $':>9}{total:,.2f}")

