class Queue:
    def __init__(self):
        self.__new_queue = list()
        #return new_queue

    def isEmpty(self):
        return len(self.__new_queue) == 0

    def length(self):
        return len(self.__new_queue)

    def enqueue(self, item):
        self.__new_queue.append(item)
        return self.__new_queue

    def dequeue(self):
        if not Queue.isEmpty(self):
            self.__new_queue.pop(0)
            return self.__new_queue
        else:
            return "CANNOT DEQUEUE FROM EMPTY QUEUE"

    def display(self):
        print(self)

newqueue = Queue()
for i in range(10):
    print(newqueue.enqueue(str(i)))
    #Queue.display(newqueue)
for i in range(12):
    print(newqueue.dequeue())
    #Queue.display(newqueue)
