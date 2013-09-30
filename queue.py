class Queue():
    def __init__(self, length):
        self.queue = []
        for i in range(length):
            self.queue.append(-1) # initialise with -1
        self.start = 0
        self.end = 0
        
    def isEmpty(self):
        total = 0
        for item in self.queue:
            total += item
        if total == -1 * len(self.queue): # check for all -1
            return True
        else:
            return False
        
    def isFull(self):
        full = True
        for item in self.queue:
            if item == -1:
                full = False # check for at least one element that is -1
        return full
    
    def insert(self, item):
        if self.isEmpty():
            self.queue[0] = item # insert first element
            self.start = 0
            self.end = 0
        elif self.isFull():
            print("Unable to insert to full queue.")
        else:
            self.queue[(self.end + 1) % len(self.queue)] = item # modulo to wrap around
            self.end = (self.end + 1) % len(self.queue) # same for shifting the end value
        print(self.queue)
        
    def delete(self):
        if self.isEmpty():
            print("Unable to delete from empty queue.")
        elif self.start == 0 and self.end == 0: # only first element to delete
            self.queue[0] = -1
        else:
            self.queue[self.start] = -1 # delete start item
            self.start = (self.start + 1) % len(self.queue) # modulo to wrap around start value
        print(self.queue)
