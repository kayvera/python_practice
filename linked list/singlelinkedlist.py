"""
A sequential collection that doesn't have to be in order, and is made up of independent nodes that can contain any data type.
Each node has a reference to the node next to it in the link. Ex) a train

elements of linked list are independent objects

insert and removals are very efficient in LL and size isnt predefined
array is better for random access

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class sLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head is None:
            print("the singly linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list doesn't exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value doesn't exist in this list"

    def deleteNode(self, location):
        if self.head is None:
            print("The SLL doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL doesn't exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = sLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)

singlyLinkedList.insertSLL(0, 0)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(3))
singlyLinkedList.deleteNode(0)
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
