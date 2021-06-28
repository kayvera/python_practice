# take a string and see if its a permutation of a palindrome, word of phrase that is same backwards and forwards

def palindromePermutation(str):
  table = createHashTable(stripString(str).lower())

  odd_counter = 0
  for k,v in table.items():
    if v % 2 != 0 and odd_counter == 0:
      odd_counter += 1
    elif v % 2 != 0 and odd_counter != 0:
      return False
  return True

def stripString(str):
    newStr = str.replace(" ", "")
    return newStr

def createHashTable(str):
    hashTable = {}
    for char in str:
        if char not in hashTable:
            hashTable[char] = 1
        else:
            hashTable[char] +=1 

    return hashTable

  

print(palindromePermutation('racecar'))