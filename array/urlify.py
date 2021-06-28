# all are both O(n) space and time

def urlify(str):
  return str.strip().replace(" ", "%20")


# or

def urlify2(str):
  return "%20".join(str.split())

# or

def urlify3(string, length):
  output = []
  for char in range(length):
      char = string[char]
      if char == ' ':
          output.append('%20')
          continue
      output.append(char)
  return ''.join(output)         
  

print(urlify("hello world  "))
print(urlify2("hello world "))
print(urlify3("hello world ", 12))