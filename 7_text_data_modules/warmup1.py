line_number = 0

with open("C:/Users/daigi/python-intro-homework/7_text_data_modules/data/notes.txt", 'r') as notes:
    for line in notes:
        line_number += 1
        print(f"Line {line_number}: {line.strip()}")
