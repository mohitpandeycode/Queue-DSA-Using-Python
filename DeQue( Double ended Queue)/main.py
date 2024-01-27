# by using list..

class Deque:
    def __init__(self):
        self.items = []

# checking empty...
    def is_empty(self):
        return len(self.items) == 0
    
# insert by front....
    def insert_front(self,data):
        self.items.append(data)

# insert by last....
    def insert_rear(self, data):
        if self.is_empty():
            self.items.append(data)
        else:
            self.items.insert(0,data)

# delete from front....
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is Empty!")

# delete from last....
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is Empty!")

#get front element...
    def get_front(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is Empty!")

#get last element....
    def get_rear(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is Empty!")


# get size of the dequeue
    def size(self):
        return len(self.items)
    


# driver code:
    
dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
dq.insert_front(40)
print("front: ",dq.get_front()," rear: ",dq.get_rear())

dq.insert_rear(50)
print("front: ",dq.get_front()," rear: ",dq.get_rear())

dq.insert_rear(60)
print("front: ",dq.get_front()," rear: ",dq.get_rear())

dq.delete_front()
print("front: ",dq.get_front()," rear: ",dq.get_rear())

dq.delete_rear()
print("front: ",dq.get_front()," rear: ",dq.get_rear())

print("size is" ,dq.size())
