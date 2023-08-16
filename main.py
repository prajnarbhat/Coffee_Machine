from Menu import *
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep


def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----' 
    
          ------ MENU ------ 
          Tea (Rs.15)
          Latte (Rs.40)
          Coffee (Rs.20)
          ------------------
    
          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    welcome()
    options = menu.read_item_data()
    user_choice = str(input(f'What would you like?\nOptions ( {options} ): ')).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
    elif menu.find_drink(user_choice) == "":
        print("Drink is not available")
        print('\033[31mError. Please choose an available option.\033[m')
    else:
        print("Drink is available")
        beverage = menu.find_drink(user_choice)  # Encapsulates the result
        sufficient_resources = coffee_maker.is_resource_sufficient(beverage.__dict__)  # TrueFalse result
        if sufficient_resources:
            sufficient_money = money_machine.make_payment(beverage.cost)
            if sufficient_money:
                coffee_maker.make_order(beverage)
                sleep(3)
        else:
            print("Please come back after sometime till we re-fill our ingredients :)")
            print('\033[31m<<THE END>>\033[m')
            is_on = False
