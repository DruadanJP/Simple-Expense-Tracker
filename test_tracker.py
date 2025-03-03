import unittest
import datetime
import json
import os
from tracker import add_expense, all_expenses, calculate_expenses, filter_category, filter_date, save_expenses

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.filename = "test_expenses.json"
        self.expenses = [
            {"amount": 50.0, "category": "Food", "date": "2025-03-01"},
            {"amount": 20.0, "category": "Transport", "date": "2025-03-02"},
            {"amount": 30.0, "category": "Food", "date": "2025-03-03"}
        ]
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_expense(self):
        new_expense = {"amount": 40.0, "category": "Entertainment", "date": "2025-03-04"}
        add_expense(self.expenses, new_expense["amount"], new_expense["category"], datetime.date(2025, 3, 4), self.filename)
        with open(self.filename, "r") as f:
            expenses = json.load(f)
        self.assertIn(new_expense, expenses)

    def test_all_expenses(self):
        # This test will just check if the function runs without errors
        try:
            all_expenses(self.filename)
        except Exception as e:
            self.fail(f"all_expenses raised an exception: {e}")

    def test_calculate_expenses(self):
        total = calculate_expenses(self.filename)
        self.assertEqual(total, 100.0)

    def test_filter_category(self):
        food_expenses = filter_category("Food", self.filename)
        self.assertEqual(len(food_expenses), 2)
        self.assertEqual(food_expenses[0]["category"], "Food")
        self.assertEqual(food_expenses[1]["category"], "Food")

    def test_filter_date(self):
        date_expenses = filter_date(datetime.date(2025, 3, 2), self.filename)
        self.assertEqual(len(date_expenses), 1)
        self.assertEqual(date_expenses[0]["date"], "2025-03-02")

    def test_save_expenses(self):
        new_expenses = [
            {"amount": 60.0, "category": "Health", "date": "2025-03-05"}
        ]
        save_expenses(new_expenses, self.filename)
        with open(self.filename, "r") as f:
            expenses = json.load(f)
        self.assertIn(new_expenses[0], expenses)

if __name__ == "__main__":
    unittest.main()