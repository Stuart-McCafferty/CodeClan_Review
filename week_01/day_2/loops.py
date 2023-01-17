# Stuart McCafferty

my_number = 3
counter = 1
value = int(input("What number am I thinking of between 1 and 5? "))

while value != my_number:
    value = int(input("Wrong! Guess again "))
    counter += 1

print("Well done! You took " + str(counter) + " guesses")

###########
total = 0
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    total += number
print(total)

############

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["age"]}')

