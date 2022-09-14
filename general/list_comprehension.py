
sloths = ["linneas", "hoffman", "pygmy", "pale-throat", "brown-throat", "maned"]

[print(sloth.capitalize()) for sloth in sloths]

sloth_string = "HelloSlothsOfTheWorld"

sloth_string= "".join([i if i.islower() else " " + i for i in sloth_string])[1:]

print(sloth_string)