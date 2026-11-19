my_dict = {"name": "Amit", "age": 18, "city": "Mumbai"}

my_dict.pop("age")

print("Updated Dictionary:", my_dict)

print("All Key-Value Pairs:")

for key, value in my_dict.items():
    print(key, ":", value)

if "name" in my_dict:
    print("Key exists")
else:
    print("Key does not exist")
