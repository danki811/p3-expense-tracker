import csv
import os
import textwrap


def main():
    while True:
        answer = input(
            textwrap.dedent("""
            Menu
            1. Add expense
            2. View expense
            3. Delete expenses
            4. Quit
            """)
        )

        if answer == "1":
            add_expense()
        elif answer == "2":
            view_expense()
        elif answer == "3":
            delete_expenses()
        elif answer == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-4.")


def add_expense():
    category = input("Category: ")
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Accept only numbers")
    description = input("Description: ")

    fieldnames = ["Category", "Amount", "Description"]
    file_name = "expenses.csv"
    file_exists = os.path.exists(file_name) and os.path.getsize(file_name) > 0
    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {"Category": category, "Amount": amount, "Description": description}
        )


def view_expense():
    file_name = "expenses.csv"
    file_exists = os.path.exists(file_name) and os.path.getsize(file_name) > 0

    if not file_exists:
        print("No expenses yet.")
        return
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        print(f"{'CATEGORY':<12} {'AMOUNT':<8} {'DESCRIPTION'}")
        print("-" * 34)
        for row in reader:
            print(
                f"{row['Category']:<12} ${float(row['Amount']):<7.2f} {row['Description']}"
            )


def delete_expenses():
    file_name = "expenses.csv"
    if os.path.exists(file_name):
        os.remove("expenses.csv")
        print("file removed")
    else:
        print("file doesn't exist")


main()
