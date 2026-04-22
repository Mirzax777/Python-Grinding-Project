class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(({'amount': -amount, 'description': description}))
            return True
        else:
            return False
        

    def get_balance(self):
        balance = 0
        for value in self.ledger:
            balance += value["amount"]
        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+ destination.name)
            destination.deposit(amount, "Transfer from "+ self.name)
            return True
        else:
            return False
        

    def check_funds(self, amount):
        balance = self.get_balance()
        if balance < amount:
            return False
        else:
            return True 

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"            
            items += f"{desc:<23}{amount:>7}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
     

def create_spend_chart(categories):
    
    spent = []
    for cat in categories:
        total = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                total += abs(entry["amount"])
        spent.append(total)

    # Step 2: Calculate percentage (rounded DOWN to nearest 10)
    total_spent = sum(spent)
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    # Step 3: Build the chart string
    chart = "Percentage spent by category\n"

    # Y-axis: 100 down to 0, step 10
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        for pct in percentages:
            row += "o  " if pct >= level else "   "
        chart += row + "\n"

    # Horizontal line (4 spaces for label + dashes per category)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 4: Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "
        for cat in categories:
            row += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += row + "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)