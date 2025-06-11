
import csv
from datetime import datetime

class Expense:
    def __init__(self, category, amount, date=None):
        self.category = category
        self.amount = float(amount)
        self.date = date if date else datetime.today().strftime('%Y-%m-%d')

class ExpenseManager:
    def __init__(self, file_name="expenses.csv"):
        self.file_name = file_name
        self.expenses = []
        self.load_from_csv()  

    def add_expense(self, category, amount, date=None):
        expense = Expense(category, amount, date)
        self.expenses.append(expense)
        self.save_to_csv()
        print(f" Expense added: {category} - ${amount} on {expense.date}")

    def view_expenses(self):
        print(" All Expenses:")
        for exp in self.expenses:
            print(f"{exp.date} | {exp.category} | ${exp.amount}")

    def category_summary(self):
        summary = {}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        print("Total Spent Per Category:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

    def save_to_csv(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount", "Date"])
            for exp in self.expenses:
                writer.writerow([exp.category, exp.amount, exp.date])

    def load_from_csv(self):
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append(Expense(row["Category"], row["Amount"], row["Date"]))
        except FileNotFoundError:
            pass  # No existing file, start fresh


manager = ExpenseManager()
while True:
    print("\n Expense Tracker Menu:")
    print("1 Add Expense")
    print("2 View Expenses")
    print("3 View Category Summary")
    print("4 Exit")
    choice = input("Select an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        manager.add_expense(category, amount, date)
    elif choice == "2":
        manager.view_expenses()
    elif choice == "3":
        manager.category_summary()
    elif choice == "4":
        print(" Exiting... Your expenses are saved.")
        break
    else:
        print(" Invalid choice. Please try again.")

