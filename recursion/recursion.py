# must have a conditional

def openRussianDoll(doll):
  if doll == 1:
    print("All dolls are opened")
  else: 
    openRussianDoll(doll-1)