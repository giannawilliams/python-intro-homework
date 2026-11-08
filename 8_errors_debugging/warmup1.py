while True:
    try:
        number = float(input("Enter a number: "))
        
        if type(number) == float:
            print(f"You entered: {number}")

        else:
            raise ValueError("That's not a valid number. Try again.")

        break

    except ValueError:
        print("That's not a valid number. Try again.")