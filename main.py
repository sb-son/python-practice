# This is a sample Python script.
import random
import numpy as np

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('hello world')

print(2+2)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def lucky_number(name):
    random_num = random.randint(1, 10)
    number = len(name) * random_num
    print("Hello " + name + ". Your lucky number is " + str(number) + ". Multiplier was " + str(random_num))

lucky_number("Kay")
lucky_number("Cameron")


# This function calculates the number of days in a variable number of
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
    # Assign a variable to hold the calculations for the number of days in
    # a year (years*365) plus the number of days in a month (months*30) plus
    # the number of days provided through the "days" parameter variable.
    my_days = (years * 365) + (months * 30) + days
    # Use the "return" keyword to send the result of the "my_days"
    # calculation to the function call.
    return my_days


# Function call with user provided parameter values.
print(find_total_days(2, 5, 23))


# This function converts fluid ounces to milliliters and returns the
# result of the conversion.
def convert_volume(fluid_ounce):
    # Calculate value of the "ml" variable using the parameter variable
    # "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
    # ounce.
    ml = fluid_ounce * 29.5
    # Return the result of the calculation.
    return ml


# Call the conversion from within the print() function using 2 fluid
# ounces. Convert the return value from a float to a string.
print("The volume in millimeters is " + str(convert_volume(2)))

# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in millimeters is " + str(convert_volume(2) * 2))
# Alternative calculation:
# print("The volume in millimeters is " + str(convert_volume(4))


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(my_trip_km * 2))


#List comprehension example
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]

print(4 * 2 % 5)

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

print((10 >= 5*2) and (10 <= 5*2))

multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")

# This function counts the number of integer factors for a
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a
# factor (n*1).
def count_factors(given_number):
    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded).
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors.
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0))  # Count value will be 0
print(count_factors(3))  # Should count 2 factors (1x3)
print(count_factors(10))  # Should count 4 factors (1x10, 2x5)
print(count_factors(24))  # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6).

mon = 7
tues = (mon + 6) % 2
tues += 3
wed = mon % 4
thu = mon * 2 + 5
wed = mon + 2 * tues
tues = mon * wed
print(tues)

count = 0
for i in range(150):
    for j in range(30):
        calc = i * j
        if calc % 10 == 0:
            count += 1

print(count)

numbers = [25, 50, 25, 50, 35, 45, 77, 21, 41, 10, 11, 22, 33, 40]
print(numbers[numbers[9]])

def fun(t, e, i):
    ret = t[:i]
    ret.append(e)
    return ret + t[i:]

lst = [8, 7, 3, 15, -4]
print(fun(lst, 'foo', 3))

weather = {
    "coord": {
        "lon": -78.64,
        "lat": 35.78
    },
    "condition": "scattered clouds",
    "main": {
        "temp": 66.16,
        "temp_min": 64,
        "temp_max": 68
    },
    "wind": {
        "speed": 9.17
    },
    "name": "Raleigh, NC"
}

np.poly1d([4, 3.1, -3.1, -1])

def mystery(country, state=None):
    new_word = ""
    if state is not None:
        for char in state:
            if char not in ['a', 'e', 'i', 'o', 'u']:
                new_word += char
    else:
        for char in country:
            if char in ['a', 'e', 'i', 'o', 'u']:
                new_word += char
    return new_word

print(mystery("United States", "Texas"))
print(mystery("United States"))

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

for n in range(6,18+1,3):
    print(n*2)

for n in range(10):
    print(n+n)

    def digits(n):
        count = 0
        if n == 0:
            count += 1
        while n != 0:  # Complete the while loop condition
            # Complete the body of the while loop. This should include
            # performing a calculation and incrementing a variable in the
            # appropriate order.
            n = n // 10
            count += 1
        return count


    print(digits(25))  # Should print 2
    print(digits(144))  # Should print 3
    print(digits(1000))  # Should print 4
    print(digits(0))  # Should print 1

for count in range(1, 6):
    print(count+1)

for outer_loop in range(2, 6 + 1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)

weather = "Rainfall"
print(weather[:4])

multiples = [x*7 for x  in range(1, 11)]
print(multiples)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

### Simple List Comprehension
print("List comprehension result:")
# The following list comprehension compacts several lines
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")
# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")
print(car_makes)

speed_limits = {"street": 35, "highway": 65, "school": 15}
print(speed_limits["highway"])
