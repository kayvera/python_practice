"""
unordered, changeable, and indexed
has a key and a value

"""
myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro'}

print('one' in myDict)  # returns true
print('uno' in myDict.values())  # returns true

for key in myDict:
    print(key, myDict[key])  # O(1)

# all() method returns boolean

newDict = {1: True, 2: True, 3: False}
print(all(newDict))
print(len(newDict))

sortDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(sortDict))
print(sorted(sortDict, reverse=True))


sortDict2 = {'ea': 1, 'aas': 2, 'udd': 3, 'seso': 4, 'wewri': 5}
print(sorted(sortDict2, key=len))
