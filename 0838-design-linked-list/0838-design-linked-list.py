
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0



    def get(self, index: int) -> int:
        if index<0 or index >= self.size:
            return -1

        temp = self.left

        for _ in range(index+1):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.left.next
        new_node.prev = self.left
        self.left.next.prev = new_node
        self.left.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev.next = new_node
        self.right.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        node = Node(val)
        prev_node = self.left
        for _ in range(index):
            prev_node = prev_node.next
        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next.prev = node
        prev_node.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self.left
        for _ in range(index + 1):
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)