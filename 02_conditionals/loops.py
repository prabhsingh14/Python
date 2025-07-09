#1
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

#2
n = 10
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print("The sum of even numbers from 1 to", n, "is", sum_even)

#3
n = 5
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print("The factorial of", n, "is", factorial)

#4
num = 29
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print(is_prime)

#5
import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1