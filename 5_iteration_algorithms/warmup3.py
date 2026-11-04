names = ["Jade", "Victoria", "Chike"]

target_name = input("Enter a name to search for: ")
print("Searching...")

name_in_list = False

for entry in names:
    if entry == target_name:
        name_in_list = True
    else:
        name_in_list = False

if name_in_list == True:
    print(f"Found {target_name} at index {names.index(target_name)} ")
    
if name_in_list == False:
    print(f"The name in {target_name} is not in the list.")