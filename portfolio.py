class Portfolio:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.positions = {}

    def buy(self, symbol, price, quantity):
        if symbol not in self.positions:
            self.positions[symbol] = {'quantity': 0, 'average_price': 0}

        self.positions[symbol]['quantity'] += quantity
        self.positions[symbol]['average_price'] = price
        self.balance -= price * quantity

    def sell(self, symbol, price, quantity):
        if symbol in self.positions and self.positions[symbol]['quantity'] >= quantity:
            self.balance += price * quantity
            self.positions[symbol]['quantity'] -= quantity
