"""
compress string so that it has the count next to the letter
aaabbbcdddd => a3b3cd4
if string can't be shortened, print original string

"""

def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    if counter:
        compressed.append(string[-1] + str(counter))

    return min(string, "".join(compressed), key=len)

def compress(string):
    temp={}
    result=""
    for x in string:
        if x in temp:
            temp[x] = temp[x]+1
        else:
            temp[x] = 1
    for key, value in temp.items():
        result += str(key) + str(value)

    return result

print(compress_string('aammmmssssss'))
print(compress('aammmmssssss'))