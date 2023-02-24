# stack 만들기
class Stack:
    def __init__(self):
        self.items = []

    #스택이 비었다면 True를 반환하고, 그렇지 않다면 False를 반환
    def empty(self):
        return not bool(self.items)

    #스택의 가장 마지막 데이터를 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환
    def pop(self):
        if not self.empty():
            return self.items.pop()

    
    #스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환
    def top(self):
        if self.items:
            return self.items[-1]

    #스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.
    def push(self, elem):
        self.items.append(elem)

    #객체자체가 Return하는 것
    def __repr__(self):
        pass
        #''.join(self.items)


    #객체를 print 했을 때 나오는 값    
    def __str__(self):
        return f'abcd'

my_list = list()
s = Stack()
s.push('test')
print(s.pop())