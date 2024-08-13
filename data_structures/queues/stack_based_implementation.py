"""
Leetcode question

https://leetcode.com/problems/implement-queue-using-stacks/submissions/1353708748/"""


class MyQueue:
    """The idea is to have two stacks called push_stack & pop_stack.

    """
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            while(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
    
    def peek(self) -> int:
        if not self.pop_stack:
            while(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()