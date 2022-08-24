class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # assigning data
        self.next = None  # initialize


class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    print(llist.head.data)
    print(llist.head.next.data)
    print(second.next.data)

