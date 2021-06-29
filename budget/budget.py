from math import floor

class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def get_withdrawls(self):
        """Gets the total amount that was withdrawled"""
        withdrawls = 0
        for transaction in self.ledger:
            amount = transaction["amount"]
            if amount < 0:
                withdrawls += abs(amount)
        return withdrawls
    
    def deposit(self, amount, description: str = ""):
        """Makes a deposit"""
        amount = abs(amount)
        self.ledger.append(
            {"amount" : amount, "description": description}
        )
    
    def withdraw(self, amount, description: str = "") -> bool:
        """Makes a withdrawl"""
        withdrawl_amount = -abs(amount)
        if self.check_funds(withdrawl_amount):
            self.ledger.append({"amount" : withdrawl_amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """Returns the balance of the category"""
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    
    def transfer(self, amount, category):
        """Transfers an amount to another category"""
        amount = -abs(amount)
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to %s"%(category.name))
            category.deposit(amount, "Transfer from %s"%(self.name))
            return True
        return False
    
    def check_funds(self, amount):
        """Checks if there are enough money left to withdrawl the amount"""
        if abs(amount)>self.get_balance(): return False
        else: return True
    
    def __str__(self) -> str:
        output = []
        output.append("{:*^30}".format(self.name))
        for transaction in self.ledger:
            output.append(
                "{:<23.23}{:>7.2f}".format(transaction["description"], transaction["amount"])
            )
        output.append(
            "Total: {}".format(self.get_balance())
        )
        
        return "\n".join(output)

def create_spend_chart(categories):
    pass