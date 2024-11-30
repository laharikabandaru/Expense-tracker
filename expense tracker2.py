import json
from datetime import datetime

# Initialize data storage
data_file = "expenses.json"
expenses = []

# Load existing data if available
try:
    with open(data_file, "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    pass

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return
    amount = input("Enter amount: ")
    if not amount.isdigit():
        print("Amount must be a number!")
        return
    description = input("Enter description: ")
    category = input("Enter category (Food, Transport, Entertainment, Others): ")
    
    expense = {
        "date": str(date),
        "amount": float(amount),
        "description": description,
        "category": category
    }
    expenses.append(expense)
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print(expense)
def analyze_expenses():
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"Total Spending: {total_spent}")

    # You can further analyze expenses by category, date range, etc.
    # For example, to calculate spending by category:
    category_expenses = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        category_expenses[category] = category_expenses.get(category, 0) + amount

    for category, amount in category_expenses.items():
        print(f"{category}: {amount}")

expenses = []


# Main menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        analyze_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please try again.")
