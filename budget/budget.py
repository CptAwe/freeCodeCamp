class Category:
    
    ledger = []
    __name = ""

    def __init__(self, name):
        self.__name = name
    
    def deposit(self, amount, description: str = ""):
        amount = abs(amount)
        self.ledger.append(
            {"amount" : amount, "description": description}
        )
    
    def withdraw(self, amount, description: str = "") -> bool:
        withdrawl_amount = -abs(amount)
        if self.check_funds(withdrawl_amount):
            self.ledger.append({"amount" : withdrawl_amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    
    def transfer(self, amount, category):
        amount = -abs(amount)
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to %s"%(category.__name))
            category.deposit(amount, "Transfer from %s"%(self.__name))
            return True
        return False
    
    def check_funds(self, amount):
        if amount>self.get_balance(): return False
        else: return True
    
    def __str__(self) -> str:
        output = []
        output.append("{:*^30}".format(self.__name))
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