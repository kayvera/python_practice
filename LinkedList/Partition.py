from linkedlistpractice import LinkedList
from linkedlistpractice import ListNode

def partition(self, head:ListNode, num):
  h1 = l1 = ListNode(0)
  h2 = l2 = ListNode(0)
  while head:
    if head.val <  num:
      l1.next = head
      l1 = l1.next
    else:
      l2.next = head
      l2 = l2.next
    head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next
  

customLL = LinkedList()
customLL.generate(10, 0, 99)
customLL.add(24)
print(customLL)
print(partition(customLL,0, 24))
