class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next

# class priority Queue
class PQueue:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start is None

# push method...
    def push(self, data, priority):
        n = Node(data, priority)
        if self.is_empty() or priority < self.start.priority:  # Checking if the queue is empty or the new element priority is smaller then the first element priority
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority: # checking if the priority of next element of temp is smaller equal then new element priority
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is out of elements!")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -=0
            return data

    def size(self):
        return self.item_count

            

pq = PQueue()
pq.push("Ashi", 1)
pq.push("Monty", 1)
pq.push("shreya", 5)
pq.push("Mohan", 5)
pq.push("rocky", 6)
pq.push("Surya", 2)
pq.push("Ram", 3)
while not pq.is_empty():
    print(pq.pop())
