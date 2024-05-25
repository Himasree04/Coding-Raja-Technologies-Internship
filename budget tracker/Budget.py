import os
import json

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def add_income(data, amount):
    data['income'] += amount
    save_data(data, 'budget_data.json')

def add_expense(data, category, amount):
    data['expenses'].append({'category': category, 'amount': amount})
    save_data(data, 'budget_data.json')

def calculate_remaining_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def analyze_expenses(data):
    expenses_by_category = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount
    return expenses_by_category

def display_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Remaining Budget")
    print("4. Analyze Expenses")
    print("5. Exit")

def main():
    file_name = 'budget_data.json'
    data = load_data(file_name)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            add_income(data, amount)
            print("Income added successfully.")
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(data, category, amount)
            print("Expense added successfully.")
        elif choice == '3':
            remaining_budget = calculate_remaining_budget(data)
            print("Remaining Budget: $", remaining_budget)
        elif choice == '4':
            expenses_by_category = analyze_expenses(data)
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(category, ": $", amount)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

