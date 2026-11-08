try:
    open('.../data/missing.txt')

except FileNotFoundError:
    print("Error: 'missing.txt' was not found. Please check the file path and try again.")