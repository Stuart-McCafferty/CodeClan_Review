meals = {"breakfast" : "toast", "lunch" : "soup", "dinner": "steak"}

print(meals)
print(meals["breakfast"])

#FOR KEYS ONLY
print("breakfast" in meals)
print("toast" in meals)

meals["supper"] = "pancakes"
print(meals)

meals["dinner"] = "pasta"
print(meals)

del(meals["breakfast"])
print(meals)

print(list(meals))
print(meals.keys())
print(meals.values())

######

countries = {
    "uk" : {
        "population" : 1000,
        "capital" : "London"
    },
    "germany" : {
        "population" : 5,
        "capital" : "Berlin"
    }
}

print(countries)
print(countries["germany"]["capital"])