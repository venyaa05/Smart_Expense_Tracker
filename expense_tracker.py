import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class ExpenseTracker:

    def __init__(self):
        self.data = pd.read_csv("expenses.csv")
        self.data["Amount"] = pd.to_numeric(self.data["Amount"], errors="coerce")
        self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")
        self.data = self.data.dropna(subset=["Amount", "Date"])

    def add_expense(self):
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            date = pd.to_datetime(date)
        except:
            print("Please enter a correct date.")
            return

        try:
            amount = float(input("Enter amount: "))
        except:
            print("Please enter a number.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")

        if amount <= 0:
            print("Amount should be greater than 0")
            return

        new_expense = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.data.loc[len(self.data)] = new_expense
        self.data.to_csv("expenses.csv", index=False)

        print("Expense added successfully!")

    def get_summary(self):
        total = np.sum(self.data["Amount"])
        average = np.mean(self.data["Amount"])

        print("\n----- Summary -----")
        print("Total Expense:", round(total, 2))
        print("Average Expense:", round(average, 2))

        print("\nCategory Wise Expense:")
        print(self.data.groupby("Category")["Amount"].sum())

    def filter_expenses(self):
        category = input("Enter category: ")

        result = self.data[
            self.data["Category"].str.lower() == category.lower()
        ]

        if result.empty:
            print("No expense found.")
        else:
            print("\nFiltered Expenses:")
            print(result)

    def generate_report(self):
        print("\n----- Expense Report -----")
        print("Total Expenses:", round(self.data["Amount"].sum(), 2))
        print("Average Expense:", round(self.data["Amount"].mean(), 2))
        print("Number of Expenses:", len(self.data))

    def show_charts(self):
        data = self.data.groupby("Category")["Amount"].sum()

        data.plot(kind="bar")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

        date_data = self.data.sort_values("Date")
        date_data.plot(x="Date", y="Amount", kind="line", marker="o")
        plt.title("Expense Trend")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()

        data.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.show()

        sns.histplot(self.data["Amount"], bins=5)
        plt.title("Expense Amounts")
        plt.xlabel("Amount")
        plt.ylabel("Frequency")
        plt.show()


tracker = ExpenseTracker()

while True:
    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Filter Expense")
    print("4. Generate Report")
    print("5. Show Charts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.add_expense()
    elif choice == "2":
        tracker.get_summary()
    elif choice == "3":
        tracker.filter_expenses()
    elif choice == "4":
        tracker.generate_report()
    elif choice == "5":
        tracker.show_charts()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Wrong choice")
