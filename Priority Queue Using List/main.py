class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
# push an element in priority queue.   
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:  # checking if the index is less then length of list and First item of index of list is smaller equal then priority
            index+=1
        self.items.insert(index,(data,priority))

# poping the first element coz it was the item with highest prority...  
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("Priority queue is out of elements")
    def size(self):
        return len(self.items)


# driver code
        
prty = Queue()
prty.push("amit",1)
prty.push("ashish",2)
prty.push("saurav",1)
while not prty.is_empty():
    print(prty.pop())
