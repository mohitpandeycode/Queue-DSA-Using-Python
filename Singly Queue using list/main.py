class Queue:     # making queue class
    def __init__(self):
       self.list = []   #defie empty list to store queue data 

# check queue is empty...
    def is_empty(self):
        return len(self.list) == 0
    
# push element in queue... 
    def enqueue(self,data):
        self.list.append(data)

# pull item from queue...  
    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("The queue is empty")

# get the front element of queue....   
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("The queue is empty")

#get the rear element of queue....
    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("The queue is empty")

# get the size of queue.... 
    def size(self):
        return len(self.list)



# Driver_code!
      
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print("front element is ",q.get_front())
print("rear element is ",q.get_rear())
print("size is",q.size())

q.dequeue()
print("after dequeue the front element is ",q.get_front())
print("rear element is ",q.get_rear())
print("size is",q.size())



