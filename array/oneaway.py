'''
three types of edits on a string: insert, remove, replace
given two strings check if the string check if there is 1 or zero edits away
'''

def oneAway(s1, s2):
  if len(s1) == len(s2):
    return oneReplace(s1, s2)
  if len(s1) + 1 == len(s2):
    return oneInsert(s1, s2)
  if len(s1) - 1 == len(s2):
    return oneInsert(s2, s1)
  return False
  

def oneReplace(s1, s2):
  edited = False
  for c1, c2 in zip(s1, s2):
    if c1 != c2:
      if edited:
        return False
      edited = True
  return True

def oneInsert(s1, s2):
  edited = False
  i, j = 0, 0
  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
      if edited:
        return False
      edited = True
      j += 1
    else:
      i += 1
      j += 1
  return True

print(oneAway('hello', 'ello'))
print(oneAway('hello', 'helle'))
print(oneAway('hello', 'helloo'))
print(oneAway('hello', 'ell'))
print(oneAway('hello', 'hello'))