a = [0, 1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

d = [0, 1]
d = d * 4
print(d)

print(len(c))
print(max(c))
print(min(c))
print(sum(c))
print(sum(c)/len(c))

my_list = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    my_list.append(value)
    average = sum(my_list)/len(my_list)

print('Average: ', average)
