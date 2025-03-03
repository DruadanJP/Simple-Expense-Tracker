import datetime
import json
import pandas as pd
import os
from tabulate import tabulate


def add_expense(expenses, amount, category, date, filename):
    date_str = date.isoformat()
    expenses.append({"amount": amount, "category": category, "date": date_str})
    save_expenses(expenses, filename)

def all_expenses(filename):
    with open(filename, "r") as f:
        expenses = json.load(f)
        df = pd.DataFrame(expenses)
    # Display the DataFrame in the terminal with nice formatting
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

def calculate_expenses(filename):
    with open(filename, "r") as f:
        return sum([expense["amount"] for expense in json.load(f)])

def filter_category(category, filename):
    with open(filename, "r") as f:
        expenses = json.load(f)
        return [expense for expense in expenses if expense["category"] == category]
    
def filter_date(date, filename):
    with open(filename, "r") as f:
        expenses = json.load(f)
        return [expense for expense in expenses if expense["date"] == date.isoformat()]
    
def save_expenses(expenses, filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_expenses = json.load(f)
            expenses = existing_expenses + expenses
        with open(filename, "w") as f:
            json.dump(expenses, f)

def get_date_input(prompt):
    while True:
        date_entry = input(prompt)
        try:
            year, month, day = map(int, date_entry.split("-"))
            return datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Please try again.")

def get_amount_input(prompt):
    while True:
        amount_entry = input(prompt)
        try:
            return float(amount_entry)
        except ValueError:
            print("Invalid amount format. Please try again.")


def main():
    expenses = []
    filename = input("Enter the name of the JSON file (e.g., month name, year): ") + ".json"
    while True:
        print("\nSimple Expense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Filter by date")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            date = get_date_input("Enter date in the format YYYY-MM-DD: ")
            amount = get_amount_input("Enter amount: ")
            category = input("Enter category: ")
            add_expense(expenses, amount, category, date, filename)
        elif choice == "2":
            all_expenses(filename)
        elif choice == "3":
            print(f"\nTotal Expenses: {calculate_expenses(filename)}$")
        elif choice == "4":
            category = input("Enter category to filter: ")
            print("\n")
            print(f"\nExpenses for {category}")
            per_category = filter_category(category, filename)
            for expense in per_category:
                print(f'Amount: {expense["amount"]}€')
        elif choice == "5":
            date = input("Enter date: ")
            print("\n")
            print(f"\nExpenses for {date}")
            per_date = filter_date(date, filename)
            for expense in per_date:
                print(f'Amount: {expense["amount"]}€')
        elif choice == "6":
            break

if __name__ == "__main__":
    main()