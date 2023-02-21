def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull(): print("Queue_Full")
    else:
        rear = (rear+1) % len(cQ) 
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front +1) % len(cQ)
        return cQ[front]

front = rear = -1