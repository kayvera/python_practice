# array holds data of specified type
# contiguous elements
# unique index
# size of array is predefined and cant be modified
# any element can be found by index in array

'''
Big o of array
                                Array   
Indexing                          Θ(1)   
Insert/delete at beginning        Θ(n)  
Insert/delete at end              Θ(1)   
Insert/delete in middle           Θ(n) 
'''

from array import *

# 1. create an array and traverse

arr = array('i', [1, 2, 3, 4, 5])

# arr = [1,2,3,4,5]

for i in arr:
    print(i)

# 2. access individual elements through indexes

print("step 2")
print(arr[0])

# 3. Append any value to the array using append() method

print("step 3")
arr.append(6)
print(arr)

# 4. Insert value in an array using insert() method

print("step 4")
arr.insert(0, 11)
print(arr)

# 5. Extend python array using extend() method

print("step 5")
arr2 = array('i', [10, 11, 12])
arr.extend(arr2)
print(arr)

# 6. Add items from list into array using fromlist() method

print("step 6")
tempList = [20, 21, 22]
arr.fromlist(tempList)
print(arr)

# 7. remove any array element using remove() method

print("step 7")
arr.remove(11)
print(arr)

# 8. Remove last array element using pop() method

print("step 8")
arr.pop()
print(arr)

# 9. fetch any element through its index using index() method

print("step 9")
print(arr.index(21))

# 10. Reverse a python array using reverse() method

print("step 10")
arr.reverse()
print(arr)

# 11. Get array buffer information through buffer_info() method

print("step 11")
print(arr.buffer_info())

# 12. Check for number of occurences of an element using count() method

print("step 12")
print(arr.count(11))

# 13. Convert array to string using tostring() method

print("step 13")
strTemp = arr.toString()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(strTemp)

# 14. Convert array to a python list with same elements using tolist() method

print("step 14")
# print(arr.tolist())

# 15. Append a string to char array using fromstring() method

print("step 15")
# look at step 13

# 16. Slice elements from an array

print("step 16")
print(arr[1:4])
