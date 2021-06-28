"""
Given two strings, write a method to see if one is a permutation of the other

"""

#worst case O(nlogn)
#best case O(n)

def checkPermutation(str1, str2):
    sort1 = "".join(sorted(stripString(str1)))
    sort2 = "".join(sorted(stripString(str2)))
    
    if sort1 == sort2:
        return True
    else:
        return False

def stripString(str):
    newStr = str.replace(" ", "")
    return newStr

# print(checkPermutation("hellow orld", "dlrowlleoh"))

def checkPermutationBetter(str1, str2):
    table1 = createHashTable(stripString(str1))
    table2 = createHashTable(stripString(str2))
    
    if table1 == table2:
        return True
    else:
        return False
    

def createHashTable(str):
    hashTable = {}
    for char in str:
        if char not in hashTable:
            hashTable[char] = 1
        else:
            hashTable[char] +=1 

    return hashTable

print(checkPermutationBetter("hellow sorld", "dlrowlleoh"))