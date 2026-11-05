name_list = ["Jade", "Victoria", "Chike"]

target_name = input("Enter a name to search for: ")
print("Searching...")

name_in_list = False
found_index = ""

for i, name in enumerate(name_list):
    if name == target_name:
        name_in_list = True
        found_index = i

if name_in_list == True:
    print(f"Found {target_name} at index {found_index}")

if name_in_list == False:
    print(f"The name in {target_name} is not in the list.")