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

# recursive uses stack memory

# recursive solution - not time and space efficient


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

# interative solution


def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power


"""
when to use recursion
- when you can break problem into smaller sub problems
- when we are fine with extra overhead(both time and space) that comes with it
- a quick solution, not efficient
- great for tree traversal
- when we use memoization in recursion

when to avoid
- if time and space complexity matters
- when you need speed

"""

# Factorial - product of all positive integers less than or equal to n
# denoted by n!
# only positive number
# 0!=1

"""
1) create recursive case - the flow

2) then base case - stopping criterion

3) unintentional case - the constraint

"""


def factorial(n):
    assert n >= 0 and int(
        n) == n, 'The number must be a positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

# fibonacci numbers
# sequence where each number is the sum of the two preceding numbers - sequence starts from 0 and 1
# f(n) = f(n-1) + f(n-2)


def fibonacci(n):
    assert n >= 0 and int(
        n) == n, 'Fibonacci number can\'t be negative number or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(4))
