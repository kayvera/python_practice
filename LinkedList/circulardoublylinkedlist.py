class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL has been created"

    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL doesn't exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"

    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not a node to reverse through")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "there isn't any nodes in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value doesn't exist in cdll"
                tempNode = tempNode.next

    def deleteNode(self, location):
        if self.head is None:
            print("There isnt any nodes to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been deleted")

    def deleteCDLL(self):
        if self.head is None:
            print("This is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.head = None
            print("The cdll has been deleted")


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 1)
circularDLL.insertCDLL(3, 1)
print(circularDLL.searchCDLL(2))
print([node.value for node in circularDLL])
circularDLL.deleteNode(2)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])
# circularDLL.traversalCDLL()
# circularDLL.reverseTraversalCDLL()
