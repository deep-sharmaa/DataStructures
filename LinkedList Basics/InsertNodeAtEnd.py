class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def MyinsertNodeAtEnd(self, newNode=69):

        tmp = self.head
        endNode = None
        print("here")
        while tmp:
            if tmp.next is None:
                endNode = tmp
                break
            tmp = tmp.next

        naya_node = Node(newNode)
        endNode.next = naya_node

    def append(self, new_data=69):  # geeks for geeks soln

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printList(self):

        tmp = self.head
        print("i am in")
        while tmp:
            print(tmp.data)

            tmp = tmp.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.append()
    ll.printList()
