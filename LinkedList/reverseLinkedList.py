class Node:
  def __init__(self, data = None, next=None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  def printLL(self):
    current = self.head 
    while(current):
      print(current.data)
      current = current.next

def reverseList(list):
  previous = None
  current = list.head
  following = current.next
  
  while current:
    current.next = previous
    previous = current
    current = following
    if following:
      following = following.next
  list.head = previous

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
reverseList(LL)
LL.printLL()

