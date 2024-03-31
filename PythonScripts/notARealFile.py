#aisfapsf
#asfasfd
#more commenets
#more usless comments
#comments
# Poor variable naming
a = 10
b = 20
z = 40
result = a + b
print("Result:", result)

# Magic numbers
def calculate_area(radius):
    return 3.14159 * (radius ** 2)

# Commented-out code
"""
def calculate_volume(radius, height):
    volume = 3.14159 * (radius ** 2) * height
    # print("Volume:", volume)
    return volume
"""

# Large function with multiple responsibilities
def process_data(data):
    processed_data = []
    for item in data:
        if item > 10:
            processed_data.append(item * 2)
        else:
            processed_data.append(item)
    return processed_data

# Duplicate code
def calculate_sum(a, b):
    return a + b

def calculate_difference(a, b):
    return a - b

# Useless comments
def greet(name):
    # This function greets the user
    print(f"Hello, {name}!")

# Long function
def long_function():
    result = 0
    for i in range(10000):
        result += i
    return result

# Unused variables
x = 5
y = 10
