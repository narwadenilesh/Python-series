chai = "Masala Chai"

print(chai[0])

slice_chai = chai[0:3]
print(slice_chai)

num_list = "0123456789"
# slicing in diff ways
num_list[:]

num_list[0:]
num_list[:6]

# num_list[0:7:2]   here third parameter is hop

# methods of strings
# chai.strip()  // removes space or trim

print(chai.replace("Masala", "Ginger"))

# convert string to list
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())

# chai = "Masala Chai"
# print(chai.find("Chai"))  if not found return -1 or return index 

chai = "masala chai chai chai"
print(chai.count("chai"))

chai_type = "Masala"
quantity = 2
#  curly braces called placeholders
order = "I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))

#  convert list to string
chai_variety = ["lemon", "Masala", "Ginger", "Mint"]
print(", ".join(chai_variety))
print("-".join(chai_variety))
print("_".join(chai_variety))

chai = "Masala chai"
print(len(chai))

# loop on string
for letter in chai:
    print(letter)

chai = "He said, \"Masala chai is awesome \" "
print(chai)

# check string contains in the given string
chai = "Masala chai"
# it check that Masala is contained in chai or not gives true or false
print("Masala" in chai)


