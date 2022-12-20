
# can pause execution and start back later
def steps(start, stop):
    for i in range(start, stop + 1, 2):
        yield i

odds = steps(3,15)

# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))

evens = steps(2,10)
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))


# generator for steps in array 
# input iterator and step through indecies to access values 

def stepping_lists(lst, step):
    for i in range(0, len(lst), step):
        yield lst[i]
    yield lst[::step]

a = [0,1,2,3,4,5,6]
stepa = stepping_lists(a, 2) 
print(stepa)
print(next(stepa))
print(next(stepa))
print(next(stepa))
print(next(stepa))
print(next(stepa))

