def add_resources(resources):
    for key in resources:
        resources[key] += int(input(f"Enter whole number amount added of {key}: "))
    return resources


def generate_report(resources):
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        elif key == "money":
            print(f"{key.title()}: ${resources[key]}")


def resource_check(menu_items, resources):
    if menu_items['ingredients']['water'] > resources['water']:
        return False, 'water'

    elif menu_items['ingredients']['milk'] > resources['milk']:
        return False, 'milk'

    elif menu_items['ingredients']['coffee'] > resources['coffee']:
        return False, 'coffee'

    return True, " "


def transaction(money_paid):
    quarters_inserted = int(input("How many quarters? "))
    dimes_inserted = int(input("How many dimes? "))
    nickles_inserted = int(input("How many nickles? "))
    pennies_inserted = int(input("How many pennies? "))

    money_paid = money_paid + (quarters_inserted * .25) + (dimes_inserted * .1) + (nickles_inserted * .05) + (pennies_inserted * .01)
    return money_paid


def make_drink(menu_item, resources):
    for key in resources:
        if key in menu_item["ingredients"]:
            resources[key] -= menu_item["ingredients"][key]

        else:
            resources[key] += menu_item['cost']

    return resources