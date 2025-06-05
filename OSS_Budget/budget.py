import datetime
from expense import Expense
from income import Income

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
    
    def add_income(self, source, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, source, description, amount)
        self.incomes.append(income)
        print("소득이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def list_incomes(self):
        if not self.incomes:
            print("소득 내역이 없습니다.\n")
            return
        print("\n[소득 목록]")
        for idx, e in enumerate(self.incomes, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


