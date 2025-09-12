list01 = [1, 2, 3, 4, 5]
print(f"Original list:", list01)
list01.append(6)
print(f"After appending 6:", list01)
list01.remove(3)
print(f"After removing 3:", list01)
list01.insert(2, 3) #insert 3 at index 2
print(f"After inserting 3 at index 2:", list01)
list01.pop()
print(f"After popping last element:", list01)
print(f"First element:", list01[0])
print(f"Last element:", list01[-1])
print(f"Elements from index 1 to 4:", list01[1:4])
print(f"Reversed list:", list01[::-1])

#operator overloading
list02 = [7, 8, 9]
combined_list = list01 + list02
print(f"Combined list:", combined_list)

strong_brew = ["chai"] * 3
print(f"Strong brew:", strong_brew)

#bytearray
#definition of bytearray: A mutable sequence of bytes, typically used to store binary data.
byte_array = bytearray([65, 66, 67])
byte_array01 = bytearray(b"Hello")
print(f"Byte array:", byte_array)
print(f"Byte array:", byte_array01 )
print(f"Byte array as string:", byte_array.decode('utf-8'))
byte_array01 = byte_array01.replace(b"Hello", b"Hi")
print(f"Byte array:", byte_array01 ) 