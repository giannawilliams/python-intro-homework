numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

print(f"== Number Cruncher ==\n1. Find Minimum\n 2. Find Maximum\n 3. Search for a number\n 4. Sort the list\n 5. Quit\n")
option = int(input("Enter an option (1-5):"))

minimum = numbers[0]
maximum = numbers[0]
n = len(numbers)

display = True

while display == True:
    if option == 1:
        for integer in numbers:
            if integer < minimum:
                minimum = integer
        print(f"Minimum: {minimum}")
        option = int(input("Enter an option (1-5):"))

    if option == 2:
        for integer in numbers:
            if integer > maximum:
                maximum = integer
        print(f"Maximum: {maximum}")
        option = int(input("Enter an option (1-5):"))

    if option == 3:
        target_number = int(input("Enter a number to search: "))
        for integer in numbers:
            if target_number not in numbers:
                print(f"{target_number} is not in the list.")
                break
            else:
                print(f"{target_number} was found at index {numbers.index(target_number)}")
                break
        option = int(input("Enter an option (1-5):"))

    if option == 4:
        for i in range(n-1):
            for j in range(n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1]= numbers[j+1], numbers[j]
        print(f"Sorted list: {numbers}")
        option = int(input("Enter an option (1-5):"))

    if option == 5:
        display = False
        print("Goodbye.")