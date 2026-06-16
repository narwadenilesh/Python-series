chai_types = {"Masala" : "Spicy", "Ginger":"zesty", "Green":"Mild"}
print(chai_types)

# get values from dict
print(chai_types["Masala"])
print(chai_types.get("Ginger"))

# update values in dict
chai_types["Green"] = "Fresh"
print(chai_types)

# loop on dict
for chai in chai_types:
    # print(chai)
    print(f"the taste of {chai} is {chai_types[chai]}")


for key, value in chai_types.items():
    print(key, value)

# check key, value exist in dict
if "Masala" in chai_types:
    print("yes i have masala chai")

# length of dictionary
print(len(chai_types))

#  add key, value in dict
chai_types["Eary Grey"] = "citrus"
print(chai_types)

# delete value from dict
chai_types.pop("Ginger")
print(chai_types)

# remove last value directly
chai_types.popitem()
print(chai_types)

# del keyword
del chai_types["Green"]
print(chai_types)

# copy values into another dict
chai_types_copy = chai_types.copy()
print(chai_types_copy)

#  dict in another dict
tea_shop = {
    "chai" :{"Masala" : "Spicy", "Ginger":"Zesty"},
    "Tea" : {"Green" : "Mild", "Black":" String"}
}
print(tea_shop)
print(tea_shop["chai"]["Ginger"])

squared_nums = {x : x**2 for x in range(6)}
print(squared_nums)

squared_nums.clear()

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
my_new_dict = dict.fromkeys(keys, keys)
print(my_new_dict)

