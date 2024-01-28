class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next
    
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.front == None
    
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self,data):
        n = Node(data,self.rear,None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
       
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is out of elements!")     
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is out of elements!")     
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is out of elements!")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Deque is out of elements!")

    def size(self):
        return self.item_count


# driver code
    
dq = Deque()
dq.insert_front(30)
dq.insert_front(40)
dq.insert_front(50)
print("front: ",dq.get_front(),"last: ",dq.get_rear())

dq.insert_rear(20)
print("front: ",dq.get_front(),"last: ",dq.get_rear())

dq.delete_front()
print("front: ",dq.get_front(),"last: ",dq.get_rear())

dq.delete_rear()
print("front: ",dq.get_front(),"last: ",dq.get_rear())

print("size is: ",dq.size())
