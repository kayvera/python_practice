
def stringRotation(s1, s2):
  if len(s1) == len(s2) != 0: #make sure they are the same length
    return s2 in s1 * 2 #return true if after two sweeps, s2 is a substring
  return False #return false if this doesnt work


print(stringRotation("CodingInterview", "erviewCodingInt"))