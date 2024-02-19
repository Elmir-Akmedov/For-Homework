"""
#- Decorators -
#A. Create a decorator named @my_decorator that simply prints a message 
#before and after the decorated function is called.

def my_decorator(func):
    def wrapper():
        print("___/___")
        func()
        print("___/___")
    return wrapper
@my_decorator
def example_function():
    print("Hello, world!")

example_function()

#B. Modify the my_decorator from task 1 to accept arguments. The decorator 
#should be able to take arguments like a message and print it before and 
#after the decorated function is called.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{a}___/___{b}")
        func(a, b)
        print(f"{a}___/___{b}")
    return wrapper
@my_decorator
def example_function(a, b):
    print("Hello, world!")

example_function(2, 3)  

#C. Create a decorator named @timer that measures the time it takes for a 
#decorated function to run. Print the elapsed time in seconds.
import time

def timer(func):
    def wrapper():
        start = time.time()
        print("___/___")
        func()
        print("___/___")
        end = time.time()
        print(end - start)
    return wrapper
@timer
def example_function():
    print("Hello, world!")

example_function()

#D. Extend the timer decorator from Task C to accept a parameter specifying 
#the time units (e.g., seconds, milliseconds, microseconds) for printing the 
#elapsed time.

import time

def timer(unit):
    def decorator(func):
        def wrapper():
            start = time.time()
            print("___/___")
            func()
            print("___/___")
            end = time.time()
            elapsed_time = end - start
            if unit == "seconds":
                print(f"Elapsed time: {elapsed_time:.4f} seconds")
        return wrapper
    return decorator
@timer("seconds")
def example_function():
    print("Hello, world!")

example_function()

#E. Implement a decorator @log_calls that logs function calls, including 
#function name, arguments, and return value.

def log_calls(func):
    def wrapper(*args):
        print(f"Function: {func.__name__}")
        print(*args, sep=",")
        result = func(args)
        print(result)
    return wrapper
@log_calls
def log(*args):
    return sum(*args)
log(1,2,3)

#F. Create multiple decorators and demonstrate how they can be chained to 
#decorate a single function.

def outer_decorator(func):
    print("Outer decorator")
    def wrapper():
        print("Outer wrapper-")
        func()
        print("Outer wrapper+")
    return wrapper

def inner_decorator(func):
    print("Inner decorator")
    def wrapper():
        print("Inner wrapper-")
        func()
        print("Inner wrapper+")
    return wrapper

@outer_decorator
@inner_decorator
def example_function():
    print("Example function")

example_function()

#G. Implement a decorator @check_authentication that checks if a user is 
#authenticated before calling the decorated function. If authenticated, 
#allow the function to execute; otherwise, print an authentication error message.

def check_authentication(status=False):
    def outer(func):
        def wrapper():
            if status:
                func()
            else:
                print("Authentication error")
        return wrapper
    return outer

@check_authentication(status=True)
def my_func():
    print("Hello")

my_func()

#H. Write a decorator @argument_decorator that accepts arguments and prints them 
#before and after calling the decorated function.

def argument_decorator(*args):
    def outer(func):
        def wrapper():
            print(*args, end="")
            func()
            print(*args)
        return wrapper
    return outer

@argument_decorator("***")
def my_func():
    print("Hello World!!!", end="")

my_func()

#I. Create a decorator @modify_arguments that modifies the arguments passed to the 
#decorated function. For example, double all numerical arguments.

def modify_args(*args):
    def outer(func):
        def wrapper():
            print(*args, end="")
            modified_nums = [x * 2 for x in func()]
            print(*modified_nums, sep=", ",  end="")
            print(*args)
        return wrapper
    return outer

@modify_args("***")
def my_func():
    return 2, 3, 4

my_func()

#J. Write a decorator @modify_return_value that modifies the return value of the 
#decorated function. For example, append a specific string to the return value.
#

#
#- File Import Handling -
#A. Create two Python files, main.py and helper.py. In helper.py, define a function. 
#In main.py, import the function from helper.py and use it.
from hw29 import example_function
example_function()

#B. Write a Python script that imports a function from another file and executes it 
#if the script is run directly. Use if __name__ == "__main__" to control the execution.
from hw29 import example_function
example_function()


#C. Extend task 2 by passing arguments to the function imported from another file. 
#Demonstrate how the imported function can interact with the arguments provided in the main script.
from hw25 import greet_names
names_list = input(">> ").split()
greeting = greet_names(names_list)
print(greeting)
print(greeting)

#D. Write a Python script that imports all functions from another module using from module import *. 
#Demonstrate the usage of these imported functions.
from hw25 import greet_names

names_list = input(">> ").split()  
greeting = greet_names(names_list)
"""
#Quiz.
#1. Which of the following is a valid example of a decorator in Python?
#    b)
#    def my_decorator(func):
#        def wrapper():
#            print("Before function call")
#            func()
#            print("After function call")
#        return wrapper
#
#2. Consider the following decorator and decorated function snippet. 
#What does the decorator @my_decorator do when applied to my_function?
#    def my_decorator(func):
#        def wrapper(*args, **kwargs):
#            print("Decorator: Before function call")
#            result = func(*args, **kwargs)
#            print("Decorator: After function call")
#            return result
#        return wrapper
#
#    @my_decorator
#    def my_function(arg1, arg2):
#        print(f"Function called with args: {arg1}, {arg2}")
#
#    my_function("hello", 42)
#
#    c) Prints "Decorator: Before function call", calls the decorated function, 
#    prints "Decorator: After function call", and then prints the arguments passed 
#    to the decorated function.
#
#3. In the context of passing arguments to a decorated function, what does the 
#*args parameter in the decorator's wrapper function represent?
#    a) It allows passing multiple positional arguments to the decorated function.
#
#4. Consider the following Python script. What will be the output if the script is run directly?
#    def my_function():
#        print("My function in main script")
#
#    if __name__ == "__main__":
#        print("Script running directly")
#        my_function()
#
#    b) Script running directly
#    My function in main script
#
#5. In the context of using if __name__ == "__main__", why is this construct useful in Python scripts?
#    a) It allows the script to define a main function and execute it only when the script is run directly.
#
#6. Consider the following Python script and another script importing it. 
#What will be the output when the importing script is run?
#    my_module.py:
#        def my_function():
#            print("My function in my_module")
#
#        if __name__ == "__main__":
#            print("Script running directly in my_module")
#            my_function()
#
#    main_script.py:
#        import my_module
#
#        if __name__ == "__main__":
#            print("Script running directly in main_script")
#            my_module.my_function()
#
#    d) My function in my_module        
#"""