tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)

# indexing starts from zero
print(tea_varities[-1])
print(tea_varities[:])
print(tea_varities[2:])
print(tea_varities[:3])

#  last index is not included remember it
print(tea_varities[1:3])  

# update the list
tea_varities[1] = "Herbal"
print(tea_varities)

# updaye one or more in one assignment
# tea_varities[1:2] = "Lemon"
# print(tea_varities)

tea_varities[1:2] = ["Lemon"]
print(tea_varities)
tea_varities[1:3] = ["Lemon", "Mint"]
print(tea_varities)

tea_varities[1:1] = ["test", "test"]
print(tea_varities)

# insert nothing means delete operation
tea_varities[1:3] = []
print(tea_varities)

# loop on list
for tea in tea_varities:
    print(tea)

# there is another parameter also called end
# for tea in tea_varities:
#     print(tea, end= "-")

if "White" in tea_varities:
    print("i have white tea")

# append in list it appends at the end
tea_varities.append("Oolong")
print(tea_varities)

# pop methods removes last value. pop returns the remoevd value
print(tea_varities.pop())
print(tea_varities)

# insert in list at any index . its compulsory to give two argument first one is index another is value
tea_varities.insert(1, "small")
print(tea_varities)

# copy of list
# this shares the same reference
tea_variety_copy = tea_varities

# but if i want the two diff references
tea_variety_copy = tea_varities.copy()


# range in list
print(range(0, 10))

# list comprehension. diff syntax
squared_nums = [x**2 for x in range(10)]
print(squared_nums)

# cube nums 
#  last range in not included
# example range(10) then 10 is not included
cube_nums = [x**3 for x in range(5)]
print(cube_nums)


