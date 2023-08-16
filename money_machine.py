class MoneyMachine:
    CURRENCY = "Rs."

    COIN_VALUES = {
        "five": 5,
    }

    def __init__(self):
        self.collection = 0
        self.money_received = 0

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print('''\033[33m
        We accept the following coins:
        Five Rupees (Rs.5)\033[m
        ''')
        self.money_received += int(input(f"How many {MoneyMachine.COIN_VALUES.get('five')}? Please: "))
        self.money_received *= MoneyMachine.COIN_VALUES.get('five')
        print(f'You have provided: {self.CURRENCY}{self.money_received}')
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received > cost:
            change = self.money_received - cost
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.collection += cost
            self.money_received = 0
            return True
        elif self.money_received < cost:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        else:
            print("Thank you ! Your Order is confirmed. Please hang on a moment while we prepare your order :)")
            self.collection += cost
            self.money_received = 0
            return True
