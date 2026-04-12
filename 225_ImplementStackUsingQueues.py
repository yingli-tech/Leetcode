class MyStack:

    def __init__(self):
        # qm means major q, used for popping and top element
        # q means minor q, used for pushing new element
        self.qm = []
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        while self.qm:
            self.q.append(self.qm.pop(0))
        # Switch the two queues
        self.qm, self.q = self.q, self.qm

    def pop(self) -> int:
        return self.qm.pop(0)    

    def top(self) -> int:
        return self.qm[0]     
        

    def empty(self) -> bool:
        if self.qm:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()