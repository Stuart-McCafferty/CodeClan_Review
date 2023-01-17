# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]


even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

max_number = max(numbers)
min_number = min(numbers)
print(max_number - min_number)

previous = 0
for number in numbers: 
    if number == previous and number == 2:
        print("Found!")
    previous = number

total = 0
isFound = False
for number in numbers:
    if number == 6:
        isFound = True
    if isFound == False:
        print(number)
        total += number
    if number == 7:
        isFound = False
print(total)


total2 = 0
index = 0
isFound = False
for number in numbers:
    if number == 13 or numbers[index - 1] == 13:
        isFound = True
        print("TEST")
    if isFound == False:
        total2 += number
    index += 1
    isFound = False
print(total2)


total3 = 0
for number in numbers:
    total3 += number

print(total3 - 99 - 13)



# 1. Print out a list of the even integers:
# 2. Print the difference between the largest and smallest value:
# 3. Print True if the list contains a 2 next to a 2 somewhere.
# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 