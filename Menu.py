import json
import os
from types import SimpleNamespace


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, ingredients, cost):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu(MenuItem):
    """Models the Menu with drinks."""

    def __init__(self, name="", ingredients="", cost=""):
        super().__init__(name, ingredients, cost)
        if not os.path.exists('./ingredients.txt'):
            self.menu = [
                MenuItem(name="latte", ingredients={"water": 200, "milk": 150, "coffee": 24, "Tea": 0}, cost=40),
                MenuItem(name="tea", ingredients={"water": 50, "milk": 100, "coffee": 0, "Tea": 10}, cost=15),
                MenuItem(name="coffee", ingredients={"water": 50, "milk": 250, "coffee": 24, "Tea": 0}, cost=20),
            ]
            f = open('ingredients.txt', 'w')
            for item in self.menu:
                f.write(json.dumps(item.__dict__) + '\n')

    @staticmethod
    def read_item_data():
        """Returns all the names of the available menu items"""
        options = set()
        f = open('ingredients.txt', 'r')
        for item in f.readlines():
            # Parse JSON into an object with attributes corresponding to dict keys.
            line = json.loads(item, object_hook=lambda d: SimpleNamespace(**d))

            options.add(line.name)
        available_options = ' / '.join(options)
        return available_options

    @staticmethod
    def find_drink(order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        f = open('ingredients.txt', 'r')
        count = 0
        line_json = ""
        for line in f.readlines():
            line_json = json.loads(line, object_hook=lambda d: SimpleNamespace(**d))
            if order_name.lower() == line_json.name.lower():
                count += 1
                break
        if count > 0:
            return line_json
        else:
            line_json = ""
            return line_json
