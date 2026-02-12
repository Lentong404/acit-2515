# tuple = ( ) | set = { } or set( ) | dictionary = { } | list = [ ]


'''
1. A position argument is an argument that is passed through a function in the same order is defined.
function (a, b)
print (1, 2)
1 is passed to a and 2 is passed to b

2. Kwargs or keyword arguments are arguments that get passed as a parameter 
function (a, b)

print (b='something', a='something')
b will always be whatever is defined, even if the position is different.
'''



### ARGS #### 

'''
Pass * in a function and itll pack the arguments received into a tuple
Pass * to a tuple, and itll unpack everything
'''

# Unpacking a list into function arguments
def add_three_numbers(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = add_three_numbers(*numbers)  # Same as add_three_numbers(1, 2, 3)
print(result)  # 6


# Unpacking in list creation
'''
You have two lists. 
combined makes the *args unpack these two lists into one list which is combined
'''
first_list = [1, 2, 3]
second_list = [4, 5, 6]
combined = [*first_list, *second_list]  # [1, 2, 3, 4, 5, 6]
print(combined)

# Packing into a tuple

def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all(5))                  # 5
print(sum_all())                   # 0


### KWARGS #### 
'''
Pass ** in a function and itll pack the keyword arguments received into a dictionary
Pass ** to a dictionary, and itll unpack everything in key:value pairs or keyword arguments like name="Alice" age=24

'''

# Unpacking a dictionary into keyword arguments
def greet(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

person = {"name": "Alice", "age": 30, "city": "Vancouver"}
message = greet(**person)  # Same as greet(name="Alice", age=30, city="Vancouver")
print(message)

# Unpacking in dictionary creation
defaults = {"color": "blue", "size": "medium"}
custom = {"size": "large", "style": "modern"}
merged = {**defaults, **custom}  # {"color": "blue", "size": "large", "style": "modern"}
print(merged)  # Note: custom["size"] overwrites defaults["size"]



#Regular parameters must come before *args 
'''
Hello gets stuck into greeting
All the names get funneled into a tuple via *names which packs them together
'''
def greet_multiple(greeting, *names):
    """Greet multiple people with the same greeting"""
    for name in names:
        print(f"{greeting}, {name}!")

greet_multiple("Hello", "Alice", "Bob", "Charlie")




### FORWARDING ARGUMENTS ######

'''
Decorator functions let you add additional operations? functions? to an existing function
    Its like adding side sauces to a main dish!

multiply() is wrapped in a function called logger 

logger() takes the multiply function() and passes it into func. 
    looks like: multiply = logger(multiply(2,3,4))

but logger only defines wrapper - it returns wrapper
    wrapper runs by taking arguments and sticking them into a tuple...
    it prints func.__name__ which is the func's name which is multiply and the args which is the tuple...
    
    stores in return func(*args) which is multiply but unpacks the args...
    returns the multiply function (func) packs the arguments 

    wrapper is returned because its a function that needs to go before multiply first

You dont need *args or **kwargs in decorators, but it allows the decorator to accept keyword/positional arguments
    *args in a function, accepts positional arguments and sticks them in a tuple
    **kwargs in a function, accepts keyword arguments and sticks them in a dictionary
'''

def logger(func):
    """Decorator that logs function calls"""
    def wrapper(*args):  # Accept any positional arguments
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args)  # Pass them along to the original function
        return result
    return wrapper

@logger
def multiply(a, b, c):
    return a * b * c

multiply(2, 3, 4)
# Output: Calling multiply with args: (2, 3, 4)

'''
1. multiply is called with the positional arguments 2, 3, 4
2. logger is a decorator function that wraps multiply. Logger passes multiply into func
3. logger swaps multiply with wrapper. Wrapper runs. 
4. wrapper packs positional arguments into a tuple
5. Prints func's name (which is multiply) and the args tuple
6. result variable created to store func(*args) which is multiply and unpacking because a tuple was passed into it
7. Returns result which is multiply a*b*c

'''