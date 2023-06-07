# Sample Test Cases:
# summation_squared(5)   returns 55
# summation_squared(2)   returns 5
# summation_squared(10) returns 385

def summation_squared(number):
    result = 0
    for i in range(number + 1):
        result += i**2
    return result

print(summation_squared(5))   #returns 55
print(summation_squared(2))   #returns 5
print(summation_squared(10))  #returns 385