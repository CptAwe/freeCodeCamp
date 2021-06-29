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

def create_spend_chart(categories: list):
    """Creates a rudimentary bar chart"""

    BAR = "o"
    TITLE = "Percentage spent by category"
    
    withdrawls = {}
    names = []
    for category in categories:
        amount = category.get_withdrawls()
        # Why use floor() instead of int():
        # https://stackoverflow.com/a/31195540
        amount = int(floor(amount/10.)*10)
        withdrawls[category.name] = amount
    
        names.append([letter for letter in category.name])

    # Make the bars
    percentages_lines = []
    for percentage in range(100, -10, -10):
        percentages_line = "{:3}|".format(percentage)
        for category_name in withdrawls:
            if withdrawls[category_name] >= percentage:
                percentages_line += " " + BAR + " "
            else:
                percentages_line += "   "
        percentages_lines.append(percentages_line)

    # Make the horizontal line
    horizontal_line = "    {}".format("---"*len(categories) + "-")
    
    # Make the names
    bar_names_lines = []
    # find the length of the longest name
    max_name_len = max([len(name) for name in withdrawls])
    for line_num in range(max_name_len):
        bar_names_line = "    "
        for category_name in withdrawls:
            if line_num < len(category_name):
                bar_names_line += " " + category_name[line_num] + " "
            else:
                bar_names_line += "   "
        bar_names_lines.append(bar_names_line)

    chart_lines = [TITLE] + percentages_lines + [horizontal_line] + bar_names_lines

    chart_lines = "\n".join(chart_lines)

    return chart_lines