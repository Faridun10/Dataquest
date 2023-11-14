class Stack(LinkedList):
    
    def push(self, data):
        self.append(data)

    def peek(self):
        return self.tail.data

    # Add pop() method here
    def pop(self):
        ret = self.tail.data
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret
    
# test
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
top = stack.pop()
print(stack.peek())
