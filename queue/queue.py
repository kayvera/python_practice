# first in first out
# utilize first coming data
# ex)point of sale system for a restaurant
# ex)printer queue
# ex)call center

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted as the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.peek())
customQueue.delete()
