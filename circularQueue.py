class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def is_empty(self):
        
        if self.front == -1:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        data = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {data}")
        return data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", end=" ")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()


cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)  
cq.display()
print(f"Front item: {cq.get_front()}")
print(f"Rear item: {cq.get_rear()}")
cq.dequeue()
cq.display()
print(f"Front item: {cq.get_front()}")
print(f"Rear item: {cq.get_rear()}")
cq.enqueue(6)
cq.display()
print(f"Front item: {cq.get_front()}")
print(f"Rear item: {cq.get_rear()}")
cq.dequeue()
cq.dequeue()
cq.display()
print(f"Front item: {cq.get_front()}")
print(f"Rear item: {cq.get_rear()}")