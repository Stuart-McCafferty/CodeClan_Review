
odd_ages = [age for age in [5, 15, 64, 27, 84, 26] if age % 2 != 0]
print(odd_ages)


chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
over_10 = [name for name in chicken_names if len(name) > 10]
first_h = [name for name in chicken_names if name.startswith("H")]
print(over_10)
print(first_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
letters = [word[0].lower() for word in words]
print(letters)
