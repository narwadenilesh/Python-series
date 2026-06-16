tea_types = ("Black", "Green", "Oolong")
# print(tea_types)

# get values
# print(tea_types[0])
# print(tea_types[-1])

# slicing
print(tea_types[:])
print(tea_types[1:])
print(tea_types[:2])

#  imp if we put thr index beyond the length of tuples then it guives empty tuple
print(tea_types[4:5]) 

print(len(tea_types))

more_tea = ("Herbal", "Earl grey")

all_teas = more_tea + tea_types
print(all_teas)

# check is exist in tuple
if "Green" in all_teas:
    print("yes i have green tea")

print(tea_types)
# tuple unpacking 
# Python takes each element from the tuple and assigns it to a corresponding variable:
(Black, Green, Oolong) = tea_types

# check type
print(type(tea_types))