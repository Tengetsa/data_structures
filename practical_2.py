class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.start_node = None

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def delete_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_end(self):
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None

    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def reverse(self):
        temp = None
        current = self.start_node

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.start_node = temp.prev

    """
    def buble_sort(self):
        s = self.start_node
        while s.next:
            if s > s.next:
                self.next, self.prev = self.prev, self.next
                s, s.next = s.next, s
    """


l1 = DoublyLinkedList()
l1.insert_start(5)
l1.insert_start(2)
l1.insert_end(12)
l1.insert_start(3)
l1.print_l()
l1.reverse()
l1.print_l()
# l1.buble_sort()
l1.print_l()

"""
l2 = DoublyLinkedList()
l2.insert_start(2)
l2.insert_start(4)
l2.insert_start(8)
l2.insert_start(10)
l2.print_l()
l2.reverse()
l2.print_l()
"""

