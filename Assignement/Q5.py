name = input("Enter your name: ")
branch = input("Enter your branch: ")
age = int(input("Enter your age: "))
city = input("Enter your home city: ")
cgpa = float(input("Enter your CGPA: "))

my_dict = {
    "name": name,
    "roll_no": roll_no,
    "branch": branch,
    "age": age,
    "city": city
}

print("\nOriginal dictionary:")
print(my_dict)

my_dict["location"] = my_dict.pop("city")

print("\ni. After renaming city to location:")
print(my_dict)

my_dict["cgpa"] = cgpa

print("\nii. After adding CGPA:")
print(my_dict)

my_dict["age"] = my_dict["age"] + 1

print("\niii. After increasing age by 1:")
print(my_dict)

dict1 = my_dict.copy()

removed_branch = dict1.pop("branch")

print("\niv. Using pop():")
print(dict1)
print("Removed branch value:", removed_branch)

dict2 = my_dict.copy()

del dict2["branch"]

print("Using del:")
print(dict2)

print("\nv. Key-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)

print("\nvi. Checking for email:")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email is not present in the dictionary.")

friend_dict = {
    "name": "Rahul",
    "roll_no": "12345678",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

print("\nvii. Friend dictionary:")
print(friend_dict)

merged_dict = {**my_dict, **friend_dict}

print("Merged dictionary:")
print(merged_dict)

string_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}
print("\nviii. Dictionary with only string values:")
print(string_dict)