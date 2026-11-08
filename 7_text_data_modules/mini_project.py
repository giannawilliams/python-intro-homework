import os

# Use os.path.exists() to verify that ../data/expenses.csv
# exists before opening it. If it doesn't, print an
# error message and stop.

path = os.path.join("C:/Users/daigi/python-intro-homework/7_text_data_modules/","data","expenses.csv")

if os.path.exists(path):
    print("expenses.csv found")
else:
    print("expenses.csv not found")

# Read ../data/expenses.csv into a list of
# dictionaries using csv.DictReader.

import csv

expenses_list = []
with open(path,'r') as expenses_csv:
    expenses = csv.DictReader(expenses_csv)
    #Convert the amount field to float for each row.
    for row in expenses:
        row['amount'] = float(row['amount'])
        expenses_list.append(row)


from datetime import datetime

current_date = datetime.now()
print(current_date.strftime("%B %d, %Y"))

my_lookup = input("Which category would you like to check?")

expenses_my_lookup = [row for row in expenses_list if row['category'] == my_lookup]
total_expenditure = round(sum(row['amount'] for row in expenses_my_lookup),2)

with open(f'{my_lookup}_report.txt', 'w') as expense_report:
    expense_report.write(f"{my_lookup} Expense Report -- Generated {current_date}\n")
    for entry in expenses_my_lookup:
        expense_report.write(f"{entry['date']} $ {entry['amount']}\n")
    expense_report.write(f"Total: ${total_expenditure}")


