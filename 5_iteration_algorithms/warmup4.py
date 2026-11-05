for current_number in range (1,30+1):
    if (current_number%5==0) and (current_number%3==0):
        print(f"{current_number}: FizzBuzz")
    elif (current_number%5==0):
        print(f"{current_number}: Buzz")
    elif (current_number%3==0):
        print(f"{current_number}: Fizz")
    else:
        print(f"{current_number}")