from operator import index


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        num = 0
        while num < index and current is not None:
            current = current.next
            num += 1
        if num == index and current is not None:
            return current.val
        else:
            return - 1
    
    # def get(self, index: int) -> int:
        # current = self.head
        # i = 0
        # while current:
        #     if i == index:
        #         return current.val
        #     current = current.next
        #     i += 1
        # return -1


    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val: int) -> None:
        lastnode = ListNode(val)        
        if self.head is None:
            self.head = lastnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = lastnode

    def addAtIndex(self, index: int, val: int) -> None:
        addnode = ListNode(val)
        current = self.head
        num = 0
        if index == 0:
           self.addAtHead(val)
        else: 
            while current is not None:
                num += 1
                current = current.next        
            if num > index:
                temp = self.head
                for _ in range(index - 1):
                    temp = temp.next
                addnode.next = temp.next
                temp.next = addnode
            elif num == index:
                self.addAtTail(val)


    def deleteAtIndex(self, index: int) -> None:
        v_head = ListNode(0)
        v_head.next = self.head
        num = 0
        current = v_head
        while num < index and current.next is not None:
            current = current.next
            num += 1
        if num == index and current.next is not None:
                current.next = current.next.next
        self.head = v_head.next            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)