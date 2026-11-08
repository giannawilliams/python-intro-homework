try:
    numerator = float(input("Enter the numerator: "))

    denominator = float(input("Enter the denominator: "))

    print(f"The quotient is {numerator/denominator}")

except ZeroDivisionError:
    print("Can't Divide by zero -- please try a non-zero denominator.")