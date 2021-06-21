# hash table should always be top of mind for a possible solution

dict = {}

dict['a'] = 1
dict['b'] = 2
dict['c'] = 3

print(dict)

print(dict['a'])

for k in dict.keys():
    print(dict[k])

for k, v in dict.items():
    print(k, ' :', v)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

hash = {k: v for k, v in zip(keys, values)}

print(hash)

arr = [0, 1, 2, 3, 4]

newHash = list(map(hash, arr))
