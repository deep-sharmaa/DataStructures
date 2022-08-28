
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, newVal):
        newHead = Node(newVal)
        newHead.next = self.head
        self.head = newHead


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    print(llist.head.data)

    second.next = third
    print(second.next.data)

    llist.push(66)

    print(llist.head.data)


