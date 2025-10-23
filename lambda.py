# Add
add = lambda x, y: x+ y
result = add(5, 3)

print("Add: ", result)

# The above is equivalent to the following

def add(x, y):
    return x + y

#Lambda with no arguments
greet = lambda: "Hello World!"
print(greet())

# Lambda with default arguments
multiply = lambda x, y=2: x * y
print("Multiply: ", multiply(5))
print("Multiply: ", multiply(5, 3))

#Using Lambda in Higher-Order Functions
# map()
numbers = [1,2,3,4]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared: ", squared)

# filter()
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens: ", evens)

# sorted()
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print("Sorted by Age: ", sorted_by_age)

# reduce()
from functools import reduce
numbers = [1,2,3,4]
product = reduce(lambda x, y: x * y, numbers)
print("Product: ", product)

# Lambda with conditional expression (Ternary)
max_value = lambda x, y: x if x > y else y
print("Max value: ", max_value(10, 20))

# Lambda as a closure
def make_multiplier(n):
    return lambda x: x * n

doubler = make_multiplier(2)
print("Doubler: ", doubler(5))

# Higher order functions
# HOFs are a fundamental concept in functional programming and Python supports them natively. An HOF is one tat does at least one of the following:
    #Takes one or more functions as arguments
    #Returns a function as its result

# Key Benefits
    # Readability
    # Composibility
    # Performance
    # Functional Style

