import json

class BudgetTracker:
    def __init__(self):
        self.income = {}
        self.expenses = {}

    def add_income(self, amount, category):
        if category in self.income:
            self.income[category] += amount
        else:
            self.income[category] = amount

    def add_expense(self, amount, category):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def save_to_file(self, filename):
        data = {'income': self.income, 'expenses': self.expenses}
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self.income = data['income']
        self.expenses = data['expenses']
        print(f"Data loaded from {filename}")

    def get_total_income(self):
        return sum(self.income.values())

    def get_total_expenses(self):
        return sum(self.expenses.values())

    def display_summary(self):
        print("\nIncome Summary:")
        for category, amount in self.income.items():
            print(f"  {category}: ${amount}")
        print("Total Income:", self.get_total_income())
        print("Expenses Summary:")
        for category, amount in self.expenses.items():
            print(f"  {category}: ${amount}")
        print("Total Expenses:", self.get_total_expenses())
        print("Net Savings:", self.get_total_income() - self.get_total_expenses())

    def user_input(self):
        print("Welcome to the Personal Finance Tracker!")
        while True:
            print("\nOptions: Add Income, Add Expense, Save, Load, Summary, Exit")
            action = input("What would you like to do? ").strip().lower()
            if action == 'add income':
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                self.add_income(amount, category)
                print("Income added.")
            elif action == 'add expense':
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                self.add_expense(amount, category)
                print("Expense added.")
            elif action == 'save':
                filename = input("Enter filename to save (e.g., data.json): ")
                self.save_to_file(filename)
            elif action == 'load':
                filename = input("Enter filename to load (e.g., data.json): ")
                self.load_from_file(filename)
            elif action == 'summary':
                self.display_summary()
            elif action == 'exit':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.user_input()
