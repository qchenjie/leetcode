import collections


class MyStack:

    def __init__(self):
        self.a = collections.deque()
        self.b = collections.deque()

    def push(self, x: int) -> None:
        self.b.append(x)
        while self.a:
            self.b.append(self.a.popleft())
        self.a, self.b = self.b, self.a

    def pop(self) -> int:
        return self.a.popleft()

    def top(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        if not self.a:
            return True
        return False


obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)
