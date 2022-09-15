
sloths = ["linneas", "hoffman", "pygmy", "pale-throat", "brown-throat", "maned"]

[print(sloth.capitalize()) for sloth in sloths]

sloth_string = "HelloSlothsOfTheWorld"

sloth_string= "".join([i if i.islower() else " " + i for i in sloth_string])[1:]

print(sloth_string)


nums = [i for i in range(1,1001)]

string = "Practice Problems to Drill List Comprehension in Your Head."

# Find numbers from 1-1000 that are divisible by 8
divisible8 = [i for i in nums if i % 8 == 0 ]
print(divisible8)

# Find all of the numbers from 1–1000 that have a 6 in them
has6 = [num for num in nums if "6" in str(num)]
print(has6)

# Count the number of spaces in a string (use string above)
number_of_spaces = len([char for char in string if char == " "])
print(number_of_spaces)

# Remove all of the vowels in a string (use string above)
remove_vowels = "".join([char for char in string if char not in ["a","e","i","o","u"]])
print(remove_vowels)

# Find all of the words in a string that are less than 5 letters (use string above)

# Use a dictionary comprehension to count the length of each word in a sentence (use string above)

# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by