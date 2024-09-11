# Creating strings
hello_str = "Hello, World!"
single_quote_str = 'This is a string with single quotes.'
multiline_str = """This is a
multiline string."""

# Printing strings
print(hello_str)
print(single_quote_str)
print(multiline_str)

# Accessing characters in a string
first_char = hello_str[0]
last_char = hello_str[-1]

print("First character:", first_char)
print("Last character:", last_char)

# Getting the length of a string
length = len(hello_str)
print("Length of the string:", length)

# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

# Changing string case
lower_str = hello_str.lower()
upper_str = hello_str.upper()

print("Lowercase:", lower_str)
print("Uppercase:", upper_str)

# Finding a substring
position = hello_str.find("World")
print("Position of 'World':", position)

# Replacing a substring
replaced_str = hello_str.replace("World", "Python")
print("Replaced String:", replaced_str)

# Splitting a string
words = hello_str.split(" ")
print("Words in the string:", words)

# Stripping whitespaces
spaced_str = "   Hello, Python!   "
stripped_str = spaced_str.strip()
print("Stripped string:", stripped_str)

# Slicing strings
str_slice = "Hello, World!"
sliced_str = str_slice[7:12]  # From index 7 up to, but not including, index 12
print(sliced_str)  # Outputs 'World'

# Iterating through each character in a string
for char in "Iteration":
    print(char, end=' ')  # Prints each character followed by a space
print()  # Prints a newline

# Joining a list of strings into a single string
words = ['Python', 'is', 'fun']
joined_str = ' '.join(words)
print(joined_str)

# Joining a list of strings into a single string
words = ['Python', 'is', 'fun']
joined_str = ' '.join(words)
print(joined_str)

# Checking if a substring exists within a string
if "fun" in joined_str:
    print("'fun' is in the string!")

# Getting user input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# Using user input in strings
introduction = f"Your name is {user_name} and you are {user_age} years old."
print(introduction)

# Capitalizing user input
capitalized_name = user_name.capitalize()
print(f"Did you mean {capitalized_name}?")

# Working with user input and string methods
favorite_color = input("Enter your favorite color: ").lower()
print(f"You said your favorite color is {favorite_color}.")

# Reversing the color string
reversed_color = favorite_color[::-1]
print(f"Your favorite color reversed is {reversed_color}.")

#A function in Python is a reusable piece of code that can take inputs, perform some actions, 
# and optionally return an output (a result). You can define a function using the def keyword, followed by a function name and 
# parentheses () containing any parameters (inputs) the function might need.

def greet(name):
    return f"Hello, {name}!"
message = greet("Alice")
print(message)  # Output: Hello, Alice!

''' Methods

A method, on the other hand, is like a function but it's attached 
to an object and is called on that object. Methods are defined within a class and
 are used to perform operations that are related to the object.when you call a method, you use the dot notation on the object. For example, 
strings in Python have methods that you can call to perform actions specific to strings.


Key Differences

Definition: Functions are defined using the def keyword and are not associated with any object. Methods are functions that are defined inside a class and are associated with objects of that class.
Call Syntax: Functions are called by their name directly followed by parentheses (), possibly with arguments inside. Methods are called on an object using dot notation (object.method()).
Scope: A function has a global scope, meaning it can be called anywhere after its definition. A method is bound to the object it belongs to and can typically only be called using that object.'''

# Function example
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)  # Output: 5

# Method example (within a class)
class Calculator:
    def multiply_numbers(self, a, b):
        return a * b

calc = Calculator()
result = calc.multiply_numbers(2, 3)
print(result)  # Output: 6

#Example
def get_snack(snack_type):
    if snack_type == "chocolate":
        return "Here's your chocolate bar!"
    elif snack_type == "chips":
        return "Here's your bag of chips!"
    else:
        return "Sorry, we don't have that snack."

# Using the function
my_snack = get_snack("chocolate")
print(my_snack)  # This prints: Here's your chocolate bar!





































words = hello_str.split(" ")
print("Words in the string:", words)