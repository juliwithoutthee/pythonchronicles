
sloths = ["linneas", "hoffman", "pygmy", "pale-throat", "brown-throat", "maned"]

[print(sloth.capitalize()) for sloth in sloths]

sloth_string = "HelloSlothsOfTheWorld"

sloth_string= "".join([i if i.islower() else " " + i for i in sloth_string])[1:]

print(sloth_string)


nums = [i for i in range(1,1001)]

test_string = "Practice Problems to Drill List Comprehension in Your Head."

# Find numbers from 1-1000 that are divisible by 8

# Find all of the numbers from 1–1000 that have a 6 in them

# Count the number of spaces in a string (use string above)

# Remove all of the vowels in a string (use string above)

# Find all of the words in a string that are less than 5 letters (use string above)

# Use a dictionary comprehension to count the length of each word in a sentence (use string above)

# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by