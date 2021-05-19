"""
tuples are immutable sequence of python objects
comparable and hashable

"""

newTuple = ('a', 'a', 'b', 'c', 'd', 'e')
newTuple1 = ('a',)
newTuple2 = tuple('abcde')

print(newTuple)
print(newTuple1)
print(newTuple2)

# tuples are O(1) time and O(n) space

print(newTuple + newTuple2)
print(newTuple * 4)

print('a' in newTuple)

# tuple methods

print(newTuple.count('a'))
print(newTuple.index('a'))

print(len(newTuple))
print(max(newTuple))
print(min(newTuple))

print(tuple([1, 2, 3, 4, 5]))  # converts list  to tuple
