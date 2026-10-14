
import csv
import os

FILE = "expenses.csv"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    try:
        amount = float(input("Amount: "))
        note = input("Note: ")

        exists = os.path.exists(FILE)
        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not exists or os.path.getsize(FILE) == 0:
                writer.writerow(["Date", "Category", "Amount", "Note"])
            writer.writerow([date, category, amount, note])

        print("Expense saved!")
    except ValueError:
        print("Enter a valid amount.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    for e in expenses:
        print(e)

def category_summary():
    totals = {}
    for e in load_expenses():
        category = e["Category"]
        totals[category] = totals.get(category, 0) + float(e["Amount"])

    if not totals:
        print("No expenses to summarize.")
    else:
        for category, total in totals.items():
            print(category, ":", round(total, 2))

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Category to filter: ").lower()
            for e in load_expenses():
                if e["Category"].lower() == category:
                    print(e)
        elif choice == "4":
            category_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
