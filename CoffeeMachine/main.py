from data import cm_data

# Starting Values
water = 0
milk = 0
coffee = 0
till = 0
running = True

def reset_inventory():
    water = cm_data.resources["water"]
    milk = cm_data.resources["milk"]
    coffee = cm_data.resources["coffee"]
    till = 0


def print_inventory():
    print("The current inventory contains the following ...")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${till}")


def make_coffee(type):
    print(f"Making {type} ...")

reset_inventory()

while running:
    action = input("What would you like to do? (espresso/latte/cappuccino): ")
    if action == "report":
        print_inventory()
    elif action == "espresso":
        make_coffee("espresso")
    elif action == "latte":
        make_coffee("latte")
    elif action == "cappuccino":
        make_coffee("cappuccino")
    elif action == "off":
        print("Shutting down ...")
        running = False
    elif action == "reload":
        reset_inventory()
    else:
        print("Invalid selection")

# TODO: Check to see if there is enough inventory to fulfill request
# TODO: Process Coins
# TODO: Check to see if the transaction was successful
# TODO: make the coffee
# TODO: Update inventory




