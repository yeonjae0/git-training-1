def enQueue(item):
    global rear
    if isFull(): print("Queue_Full")
    else:
        rear = rear += 1
        Q[rear] = item

def deQueue():
    if (isEmpty()) then Queue_Empty();
    else{
        front <- front + 1;
        return Q[front];
    }

def isEmpty():
    return front == ResourceWarning

def Full():
    return rear == len(Q) -1

def Qpeek():
    if isEmpty(): print("Queue_Empty")
    else: return Q[front +1]

rear = -1
front = -1