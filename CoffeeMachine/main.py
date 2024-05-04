from data import cm_data

# Starting Values
water = 0
milk = 0
coffee = 0
till = 0
running = True

def reset_inventory():
    global water, milk, coffee, till
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
    if check_inventory(type):
        print("Inventory check passed")
    else:
        print("Inventory check failed")
        print_inventory()


def check_inventory(type):
    if type == "espresso":
        if (water >= cm_data.MENU["espresso"]["ingredients"]["water"]
                and coffee >= cm_data.MENU["espresso"]["ingredients"]["coffee"]):
            return True
        else:
            return False
    elif type == "latte":
        if (water >= cm_data.MENU["latte"]["ingredients"]["water"]
                and milk >= cm_data.MENU["latte"]["ingredients"]["milk"]
                and coffee >= cm_data.MENU["latte"]["ingredients"]["coffee"]):
            return True
        else:
            return False
    elif type == "cappuccino":
        if (water >= cm_data.MENU["cappuccino"]["ingredients"]["water"]
                and milk >= cm_data.MENU["cappuccino"]["ingredients"]["milk"]
                and coffee >= cm_data.MENU["cappuccino"]["ingredients"]["coffee"]):
            return True
        else:
            return False
    else:
        return False

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

# TODO: Process Coins
# TODO: Check to see if the transaction was successful
# TODO: make the coffee
# TODO: Update inventory




