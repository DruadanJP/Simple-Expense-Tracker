import json  # Import the JSON module to handle JSON file operations


def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})
    save_expenses(expenses)


def print_expenses():
    with open("../expenses.json", "r") as f:
        expenses = json.load(f)
        for expense in expenses:
            print(f'Amount: {expense["amount"]}$, Category: {expense["category"]}')


def total_expenses():
    with open("../expenses.json", "r") as f:
        expenses = json.load(f)
        return sum(map(lambda expense: expense["amount"], expenses))


def filter_expenses_by_category(category):
    with open("../expenses.json", "r") as f:
        expenses = json.load(f)
        return [expense for expense in expenses if expense["category"] == category]


def save_expenses(expenses):
    with open("../expenses.json", "w") as f:
        json.dump(expenses, f)


def main():
    expenses = []
    while True:
        print("\nSimple Expense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)
        elif choice == "2":
            print("\nAll Expenses:")
            print_expenses()
        elif choice == "3":
            print(f"\nTotal Expenses: {total_expenses()}$")
        elif choice == "4":
            category = input("Enter category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(category)
            for expense in expenses_from_category:
                print(f'Amount: {expense["amount"]}€')
        elif choice == "5":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
