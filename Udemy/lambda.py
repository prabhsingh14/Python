add_1 = lambda x: x + 1
multiply = lambda x, y: x * y 
is_even = lambda x: x % 2 == 0
greet = lambda name: f"Hello, {name}!"

print(add_1(5))          # Output: 6
print(multiply(3, 4))    # Output: 12
print(is_even(10))       # Output: True
print(greet("Alice"))    # Output: Hello, Alice!

#lamda function is used to create small anonymous functions at runtime. If you are not going to reuse the function, 
# you can use lambda function instead of defining a standard function using def keyword.