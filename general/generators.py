
# can pause execution and start back later
def steps(start, stop):
    for i in range(start, stop + 1, 2):
        yield i

odds = steps(3,15)

print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))

evens = steps(2,10)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
