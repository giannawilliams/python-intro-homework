import os


print(os.getcwd())

path = os.path.join("C:/Users/daigi/python-intro-homework/7_text_data_modules/","data","expenses.csv")

if os.path.exists(path):
    print("expenses.csv found")
else:
    print("expenses.csv not found")

