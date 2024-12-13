# Write a Python program to detect the number of local variables declared in a function. 

"""__code__:

Every function in Python has a __code__ attribute.
This attribute provides access to the underlying code object, which stores information about the function, such as its bytecode, number of arguments, local variables, and more.
co_nlocals:

It is a property of the code object (__code__) and is an integer that indicates the total number of local variables used in the function."""
def count_local_variables(func):
    return func.__code__.co_nlocals

# Example function with local variables
def example_function():
    x = 10
    y = 20
    z = x + y

# Count local variables in the example function
num_locals = count_local_variables(example_function)
print(f"Number of local variables in 'example_function': {num_locals}")
