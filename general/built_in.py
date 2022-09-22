from tomlkit import boolean

# Examples of built in python functions

# abs() returns the absolute value of a given number
number = -15 
abs(number)


# any() returns True if any element of an iterable is True 
boolean_list = ['False', 'True', 'False']
result = any(boolean_list)


# all() returns True is all elements of an iterable is True
bool_list = ['True', 'True', 'True']
result2 = all(bool_list)


# bool() returns a boolean value for a specified argument
print(bool(0))
print(bool(1))


# bytearray() returns a bytearray object which is an array of given bytes
prime_numbers = [2, 3, 5, 7]
# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')


# callable() returns true if the object passed appears callable
x = 5
print(callable(x))

def testFunction():
    print("Something Something Test")

y = testFunction
print(callable(y))


