class NoSpaceError(Exception):
    pass


class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.head = 0
        self.tail = 0
        self.the_size = 0
        self.queue = []

    def add(self, e):
        if self.the_size == self.n:
            raise NoSpaceError('Queue is full')

        self.queue.append(e)
        self.tail = (self.tail + 1) % self.n
        self.the_size += 1

        return True

    def element(self):
        return self.queue[self.head]

    def offer(self, e):
        if self.the_size < self.n:
            self.add(e)
            return True

        return False

    def peek(self):
        if self.the_size == 0:
            return None

        return self.element()

    def poll(self):
        if self.the_size == 0:
            return None

        return self.remove()

    def remove(self):
        removed = self.queue[self.head]
        self.head = (self.head + 1) % self.n
        self.the_size -= 1

        return removed

    def size(self):
        return self.the_size

    def __str__(self):
        elements = [str(self.queue[(self.head + i) % self.n]) for i in range(self.the_size)]
        return '[' + ', '.join(elements) + ']'


queue1 = CircularQueue(10)

queue1.add('apple')
queue1.add('banana')
queue1.add('cherry')

# print the queue
print(f'Queue: {queue1}')

# remove the element at the front of the queue
front = queue1.remove()
print(f'Removed element: {front}')

# print the updated queue
print(f'Queue after removal: {queue1}')

# add another element to the queue
queue1.add('date')

# peek at the element at the front of the queue
peeked = queue1.peek()
print(f'Peeked element: {peeked}')

# print the updated queue
print(f'Queue after peek: {queue1}')


queue2 = CircularQueue(10)

a = [0, 1, 2, 3, 4]

for i in a:
    queue2.add(i)

# display contents of the queue.
print('Elements of queue ' + str(queue2))

# remove the head of queue.
removedele = queue2.remove()
print('removed element-' + str(removedele))

print(queue2)

# head of queue
head = queue2.peek()
print('head of queue-' + str(head))

size = queue2.size()
print('Size of queue-' + str(size))
