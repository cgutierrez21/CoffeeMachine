import data
import coffee_funcs as cf
import os
import time

os.system("clear")

MENU = data.MENU
resources = data.resources
resources_available = True
money_paid = 0


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if user_input == "off":
        break

    elif user_input == "add":
        resources = cf.add_resources(resources)
        print(resources)
        os.system("clear")


    elif user_input == "report":
        cf.generate_report(resources)
        input("Press enter to continue. ")
        os.system("clear")


    elif user_input == "espresso":
        resources_available, missing_resource = cf.resource_check(MENU[user_input], resources)
        if not resources_available:
            print(f"Sorry there isn't enough {missing_resource}.")

        else:
            money_paid = cf.transaction(money_paid)
            if money_paid < MENU['espresso']['cost']:
                print("Sorry, that's not enough money. Money refunded.")

            else:
                if money_paid > MENU['espresso']['cost']:
                    print(f"Here is your ${round(money_paid - MENU['espresso']['cost'], 2)} in change.")

                time.sleep(1)
                print("Making your espresso.")
                time.sleep(2)
                resources = cf.make_drink(MENU['espresso'], resources)
                print("Here is your espresso. Enjoy!")

        time.sleep(2)
        os.system("clear")

    elif user_input == "latte":
        resources_available, missing_resource = cf.resource_check(MENU[user_input], resources)
        if not resources_available:
            print(f"Sorry there isn't enough {missing_resource}.")

        else:
            money_paid = cf.transaction(money_paid)
            if money_paid < MENU['latte']['cost']:
                print("Sorry, that's not enough money. Money refunded.")

            else:
                if money_paid > MENU['latte']['cost']:
                    print(f"Here is your ${round(money_paid - MENU['latte']['cost'], 2)} in change.")

                time.sleep(1)
                print("Making your latte.")
                time.sleep(2)
                resources = cf.make_drink(MENU['latte'], resources)
                print("Here is your latte. Enjoy!")

        time.sleep(2)
        os.system("clear")

    elif user_input == "cappuccino":
        resources_available, missing_resource = cf.resource_check(MENU[user_input], resources)
        if not resources_available:
            print(f"Sorry there isn't enough {missing_resource}.")

        else:
            money_paid = cf.transaction(money_paid)
            if money_paid < MENU['cappuccino']['cost']:
                print("Sorry, that's not enough money. Money refunded.")

            else:
                if money_paid > MENU['cappuccino']['cost']:
                    print(f"Here is your ${round(money_paid - MENU['cappuccino']['cost'], 2)} in change.")

                time.sleep(1)
                print("Making your cappuccino.")
                time.sleep(2)
                resources = cf.make_drink(MENU['cappuccino'], resources)
                print("Here is your cappuccino. Enjoy!")

        time.sleep(2)
        os.system("clear")

