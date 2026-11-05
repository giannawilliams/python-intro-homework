while True:
    try:
        user_integer = int(input("Enter a positive integer: "))
        if (user_integer < 0) or (user_integer == 0): #while user integer is less than or equal to 0
            print("That is not a positive integer. Try again.")
            user_integer = int(input("Enter a positive integer: "))
        else:
            print(f"You entered {user_integer}.")
            break
    except ValueError:
        print("Enter a positive integer, not a character or string.")
        try:
            user_integer = int(input("Enter a positive integer: "))
        except ValueError:
            print("Enter a positive integer, not a character or string.")
        