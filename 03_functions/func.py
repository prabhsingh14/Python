#1
def square(number):
    return number ** 2

result = square(5)  
print(result) 

#2
def multiply(a, b):
    return a * b

print(multiply(3, 4))
print(multiply('a', 6))
print(multiply(3, 'b'))

#3
import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle(5)
print("Area:", area)
print("Circumference:", circumference)

#4 - lambda function
cube = lambda x: x ** 3
print(cube(3))

#5 - args: tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3))

#6
def print_all(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_all(name="Superman", power="Fly")
print_all(power="Speed")
print_all(name="Batman", power="Money", enemy="Joker")

#7
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)