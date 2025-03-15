from data import cm_data
from prettytable import PrettyTable

# DONE: Print report
# DONE: Display Menu
# DONE: Process Payment
# DONE: Check Inventory
# DONE: Update Inventory
# DONE: Take Order
# DONE: Brew coffee
# DONE: Give change
# DONE: Update Till
# DONE: Reload Inventory
# DONE: Turn off the machine
# TODO: Clear screen between runs
# TODO: Refactor to use multiple classes


class CoffeeMachine:

    def __init__(self, datafile):
        self.datafile = datafile
        self.water = datafile.resources["water"]
        self.milk = datafile.resources["milk"]
        self.coffee = datafile.resources["coffee"]
        self.till = 0

    def report(self):
        report_table = PrettyTable()
        report_table.field_names = ["Resource", "Quantity"]
        report_table.align["Resource"] = "l"
        report_table.align["Quantity"] = "r"
        report_table.border = False
        report_table.header = True
        report_table.padding_width = 2

        report_table.add_row(["Water", self.water])
        report_table.add_row(["Milk", self.milk])
        report_table.add_row(["Coffee", self.coffee])
        report_table.add_row(["Till", self.till])
        return report_table


    def validate_inventory(self, order):
        selection = list(self.datafile.MENU.items())[order - 1]
        if (self.water < selection[1]["ingredients"]["water"] or
                self.milk < selection[1]["ingredients"]["milk"] or
                self.coffee < selection[1]["ingredients"]["coffee"]):
            return False
        return True

    def update_inventory(self, order):
        self.water -= self.datafile.MENU[list(self.datafile.MENU.keys())[order - 1]]["ingredients"]["water"]
        self.milk -= self.datafile.MENU[list(self.datafile.MENU.keys())[order - 1]]["ingredients"]["milk"]
        self.coffee -= self.datafile.MENU[list(self.datafile.MENU.keys())[order - 1]]["ingredients"]["coffee"]
        return True

    def process_order(self, order):
        if order - 1 < len(self.datafile.MENU):
            if self.validate_inventory(order):
                if self.process_payment(self.datafile.MENU[list(self.datafile.MENU.keys())[order - 1]]["cost"]):
                    self.make_coffee(order)
                    return True
            else:
                print("Sorry, there is not enough resources to make your coffee.")
        elif order == 4:
            print(self.report())
        elif order == 5:
            self.reload()
        elif order == 6:
            print("Goodbye!")
        else:
            print("Invalid selection. Please try again.")
            return False
        return True

    def make_coffee(self, order):
        self.update_inventory(order)
        print("Here is your coffee. Enjoy!")
        return True

    def reload(self):
        self.water = self.datafile.resources["water"]
        self.milk = self.datafile.resources["milk"]
        self.coffee = self.datafile.resources["coffee"]
        print("The inventory has been reloaded.")
        return True

    def process_payment(self, cost) -> float:
        print("Please insert coins.")
        dollars = int(input("How many dollars? ") or '0')
        quarters = int(input("How many quarters? ") or '0')
        dimes = int(input("How many dimes? ") or '0')
        nickels = int(input("How many nickels? ") or '0')
        pennies = int(input("How many pennies? ") or '0')
        total = (dollars * 1) + (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        if total >= cost:
            change_due = total - cost
            self.till += cost
            print(f"Thank you for your payment. Your change is ${change_due:.2f}")
            return True
        else:
            print(f"Sorry, that's not enough money. {total} refunded.")
            return False

class MenuMaker:
    def __init__(self):
        pass

    @staticmethod
    def display_menu():
        print("What would you like ...")
        print("1. Espresso")
        print("2. Latte")
        print("3. Cappuccino")
        print("4. Report")
        print("5. Reload")
        print("6. Off")
        return True


def __main__():
    is_on = True
    mm = MenuMaker()
    my_machine = CoffeeMachine(cm_data)
    while is_on:
        selection = int(input(f"{mm.display_menu()} Enter your selection: "))
        if selection == 6:
            is_on = False
        my_machine.process_order(selection)


if __name__ == "__main__":
    __main__()
