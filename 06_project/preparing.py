#1
file = open("test.txt", "w")

try:
    file.write("Hello, World!")
finally:
    file.close()

#2
with open("test.txt", "w") as file:
    file.write("Hello, World!")

