# must have a conditional

def openRussianDoll(doll):
  if doll == 1:
    print("All dolls are opened")
  else: 
    openRussianDoll(doll-1) 

# when to choose recursion

"""

if you can define the problem into similar sub problems
design an algo to compute nth
write code to list the n
implement a method to compute all

"""

# common in trees and graphs

# used in divide and conquer, greedy, and DP

def recursiveMethod(n):
  if n < 1:
    print("n is less than 1")
  else: 
    recursiveMethod(n-1)
    print(n)