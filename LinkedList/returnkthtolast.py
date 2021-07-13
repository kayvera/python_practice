# kth to last element of single linked list

from linkedlistpractice import LinkedList

def kthToLast(ll, n):
  p1 = ll.head
  p2 = ll.head
  
  for i in range(n):
    if p2 is None:
      return None
    p2 = p2.next
  while p2:
    p1 = p1.next
    p2 = p2.next
  return p1

customLL = LinkedList()
customLL.generate(5, 0, 99)
print(customLL)
print(kthToLast(customLL, 3))