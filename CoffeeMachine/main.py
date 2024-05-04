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
    print(f"Till: ${till}")


def process_coins():
    print("Please insert coins ...")
    quarters = int(input("How many quarters? ") or '0')
    dimes = int(input("How many dimes? ") or '0')
    nickels = int(input("How many nickels? ") or '0')
    pennies = int(input("How many pennies? ") or '0')
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def take_payment(type):
    global till
    payment = process_coins()
    print(f"You inserted ${payment:.2f}")
    if payment >= cm_data.MENU[type]["cost"]:
        change = payment - cm_data.MENU[type]["cost"]
        print(f"Here is your change ${change:.2f}")
        till += cm_data.MENU[type]["cost"]
        return True
    else:
        print("Insufficient funds")
        return False


def make_coffee(type):
    global water, milk, coffee, till
    print(f"Making {type} ...")
    if check_inventory(type):
        print(f"Now brewing your {type} ...")
        if type == "espresso":
            water -= cm_data.MENU[type]["ingredients"]["water"]
            coffee -= cm_data.MENU[type]["ingredients"]["coffee"]
        else:
            water -= cm_data.MENU[type]["ingredients"]["water"]
            milk -= cm_data.MENU[type]["ingredients"]["milk"]
            coffee -= cm_data.MENU[type]["ingredients"]["coffee"]
    else:
        print("Unable to make coffee, insufficient inventory.")
        print(f"refunding ${cm_data.MENU[type]['cost']:0.2f}")
        till -= cm_data.MENU[type]["cost"]


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
        if take_payment("espresso"):
            make_coffee("espresso")
    elif action == "latte":
        if take_payment("latte"):
            make_coffee("latte")
    elif action == "cappuccino":
        if take_payment("cappuccino"):
            make_coffee("cappuccino")
    elif action == "off":
        print("Shutting down ...")
        running = False
    elif action == "reload":
        reset_inventory()
    else:
        print("Invalid selection")

# TODO: Check to see if the transaction was successful





