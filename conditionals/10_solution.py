species = input("Enter pet species (Dog/Cat): ").strip().lower()
age = int(input("Enter pet age in years: "))

if species == "dog":
    if age < 2:
        recommendation = "Puppy food"
    elif age > 7:
        recommendation = "Senior dog food"
    else:
        recommendation = "Adult dog food"

elif species == "cat":
    if age < 2:
        recommendation = "Kitten food"
    elif age > 5:
        recommendation = "Senior cat food"
    else:
        recommendation = "Adult cat food"

else:
    recommendation = "Unknown pet species"

print("Recommended food:", recommendation)