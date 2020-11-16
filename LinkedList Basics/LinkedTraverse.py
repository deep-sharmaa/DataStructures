class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self): # print all the nodes
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, new_data):  # pushing at the front of the linkedList
        # Time complexity pf push() is 0(1) as it does constant amount of work
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # This function Inserts a new node after the given prev_node.

    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print
            "The given previous node must inLinkedList."
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # This function Appends a new node at the end.
    
    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node


if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(10)