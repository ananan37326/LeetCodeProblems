import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        if self.stack.__len__() == 0:
            return None
        return self.stack[0]

    def empty(self) -> bool:
        return self.stack.__len__() == 0

# Your MyStack object will be instantiated and called as such:
# myStack = MyStack()
# myStack.push(1)
# print(myStack.stack)
# myStack.push(2)
# print(myStack.stack)
# print(myStack.top()) #return 2
# print(myStack.pop()) #return 2
# print(myStack.empty()) #return False