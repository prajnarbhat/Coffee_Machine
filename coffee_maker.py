import json
import os
from types import SimpleNamespace


class CoffeeMaker:
    """Models the machine that makes the coffee"""

    resources_available = '{ "water":100, "milk":200, "coffee":100, "Tea":50, "money_collected": 0}'

    def __init__(self):
        if os.path.exists('resources.txt'):
            f = open("resources.txt", "r").readline()
            self.resources = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))
        else:
            f = open("resources.txt", "w")
            self.resources = json.loads(CoffeeMaker.resources_available,
                                        object_hook=lambda d: SimpleNamespace(**d))
            f.write(json.dumps(self.resources.__dict__))

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources.water}ml")
        print(f"Milk: {self.resources.milk}ml")
        print(f"Coffee: {self.resources.coffee}g")
        print(f"Tea: {self.resources.Tea}g")
        print()
        print(f"Total Collection: Rs.{self.resources.money_collected}")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        ingredients = drink['ingredients'].__dict__
        not_enough = []
        if ingredients['water'] > self.resources.water:
            can_make = False
            not_enough.append("water")
        if ingredients['milk'] > self.resources.milk:
            can_make = False
            not_enough.append("milk")
        if ingredients['coffee'] > self.resources.coffee:
            can_make = False
            not_enough.append("coffee")
        if ingredients['Tea'] > self.resources.Tea:
            can_make = False
            not_enough.append("tea")

        if not can_make:
            items = ",".join(not_enough)
            print(f"Sorry there is not enough {items}.")
        return can_make

    def make_order(self, order):
        """Deducts the required ingredients from the resources and makes the order."""
        ing = order.ingredients.__dict__
        price = order.cost
        for key, value in ing.items():
            self.resources.__dict__[key] -= value

        key = "money_collected"
        self.resources.__dict__[key] += price

        with open("resources.txt", "w") as f:
            f.write(json.dumps(self.resources.__dict__))

        print(f'''
                 )))
                (((
              +-----+
              |     |] - Here's your {order.name}. Enjoy! :)
              `-----'
            ''')
