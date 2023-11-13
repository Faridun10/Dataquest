class Queue(LinkedList):
    
    def enqueue(self, data):
        self.prepend(data)
        
    def get_front(self):
        return self.tail.data
    
    # Add dequeue() method here
    def dequeue(self):
        ret = self.tail.data
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret
    
    
#test
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
front = queue.dequeue()
print(queue.get_front())

# calculating wait times
processes["Wait"] = processes["Start"] - processes["Arrival"]
average_wait_time = processes["Wait"].mean()
print(average_wait_time)

# calculating Turnaround times
processes["Turnaround"] = processes["End"] - processes["Arrival"]
average_turnaround_time = processes["Turnaround"].mean()
print(average_turnaround_time)
