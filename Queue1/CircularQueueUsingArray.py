#circular Queue using Array
class CircularQueue:
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.list1 = [None]*size

    def enque(self,data):
        if (self.rear+1 % self.size == self.front):
            print("Queue is Full")
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.list1[self.rear] = data
        else:
            self.rear = ((self.rear + 1) % self.size)
            self.list1[self.rear] = data
        return

    def dequeu(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            data = self.list1[self.front]
            self.front = self.front +1
            self.rear = -1
        else:
            data = self.list1[self.front]
            self.front = (self.front + 1) % self.size
            return data

    def print_queue(self):
        # condition for empty queue
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.list1[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.list1[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.list1[i], end=" ")
            print()



q = CircularQueue(5)
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.print_queue()
q.enque(1)
q.dequeu()
q.print_queue()
q.enque(8)
q.print_queue()