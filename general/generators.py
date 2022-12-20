
# can pause execution and start back later
def odds(start, stop):
    for i in range(start, stop + 1, 2):
        yield i

g = odds(3,15)

print(next(g))
print(next(g))
print(next(g))

