from linkedlistpractice import LinkedList

def middleOfList(self):
	tortoise = self.head
	hare = self.head
	while hare and hare.next:
		tortoise = tortoise.next
		hare = hare.next.next
	return tortoise
  
  

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(middleOfList(customLL))

