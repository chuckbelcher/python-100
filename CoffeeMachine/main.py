from data import cm_data

#starting values
water = 0
milk = 0
coffee = 0
till = 0


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

# TODO: Allow user to make a request
# TODO: Check to see if there is enough inventory to fulfill request
# TODO: Process Coins
# TODO: Check to see if the transaction was successful
# TODO: make the coffee
# TODO: Update inventory
# TODO: Reload Inventory

reset_inventory()
print_inventory()
