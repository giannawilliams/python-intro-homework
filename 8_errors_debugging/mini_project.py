import os, csv

path = os.path.join("C:/Users/daigi/python-intro-homework/8_errors_debugging/data/messy_data.csv")

rows_attempted = 0
rows_parsed = 0
rows_skipped = 0
successfully_parsed_rows = []
skipped_rows = []

try:
    with open(path, 'r') as messy_data_csv:
        reader = csv.DictReader(messy_data_csv)
        try:
            for row in reader:
                rows_attempted += 1
                if None in row:
                    rows_skipped +=1
                    skipped_rows.append(f"Row {rows_attempted}: extra column detected — skipped")
                    continue

                try:
                    row['name'] = str(row['name'])
                    row['amount'] = float(row['amount'])
                    row['category'] = str(row['category'])
                
                    rows_parsed+=1
                    successfully_parsed_rows.append(row)
                
                except ValueError:
                    rows_skipped +=1
                    skipped_rows.append(f"Row {rows_attempted}: ValueError — could not convert to float")
                    print(f"Row {rows_attempted}: ValueError — could not convert value to float")

                except KeyError:
                    skipped_rows.append(row)
                    print(f"Row {rows_attempted}: KeyError -- Missing expected column")
                

        except ValueError:
            rows_skipped +=1
            skipped_rows.append(row)
            print(f"Row {rows_attempted}: ValueError -- could not convert {row} to float")
        except KeyError:
            skipped_rows.append(row)
            print(f"Row {rows_attempted}: KeyError -- Missing expected column")

except FileNotFoundError:
    print("Error: 'messy_data.csv' was not found. Please check the file path and try again.")


print(f"== CSV Report == \n Rows attempted: {rows_attempted} \n Rows parsed: {rows_parsed} \n Rows skipped: {rows_skipped}\n\n Skipped rows: {skipped_rows}")
print("Clean data")
for item in successfully_parsed_rows:
    print(f"{item['name']} | {item['category']} | {item['amount']}")