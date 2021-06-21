# check to see that string has all unique characters

def isUnique(str):
    dict = {}
    for char in str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

        if dict[char] == 2:
            return False
        else:
            return True


print(isUnique("welcom"))
