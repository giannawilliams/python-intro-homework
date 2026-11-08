import csv
with open("C:/Users/daigi/python-intro-homework/7_text_data_modules/data/students.csv", 'r') as student_csv:
    reader = csv.DictReader(student_csv)
    for row in reader:
        print(f"{row['name'] }: {row['score']}")