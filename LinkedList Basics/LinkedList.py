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

    def printList(self):  # to print all elements inside the linkedlist
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(1)
    print('llist.head')
    # print(llist.head.next)
    second = Node(5)
    third = Node(3)
    llist.head.next = second
    second.next = third

    print(llist.head.data)
    print(second.next.data)

    llist.printList()

