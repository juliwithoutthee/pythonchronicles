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


# classmethod() returns a class method for a given function 
class Student:
  marks = 0

  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)

# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

# Output: Obtained Marks: 88


# complex() takes two parameters real, imag and returns a complex num or str to complex num
# A complex num has a real part and an imaginary part (A+Bi) or (A+Bj)
z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)


# delattr(obj, name) deletes an attribute from the object 

class Coordinate:
  x = 15
  y = -10
  z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)


# dict(**kwarg) dict(mapping, **kwarg) dict(iterable, **kwarg) creates a dictionary
new_dictionary = dict(x = 3, y = 100)
print(new_dictionary)

