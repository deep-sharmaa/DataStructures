class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):  # print all the nodes
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):  # pushing at the front of the linkedList
        # Time complexity pf push() is 0(1) as it does constant amount of work
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def DeleteNode(self, key):

        tmp = self.head
        if tmp.data == key:
            self.head = tmp.next
            tmp = None
            return

        while tmp is not None:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp == None:
            return

        prev.next = tmp.next

        tmp = None

    def DeleteNodeatPosition(self, position):
        if position is None:
            return

        if position == 0:
            if self.head is not None:
                self.head = self.head.next
                return

        prev = self.head
        count = 0
        while prev.next is not None:
            nxt = prev.next
            count += 1
            if count == position:
                prev.next = nxt.next
                break
            prev = nxt
        print("Done deletion")


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)


    llist.head.next = second
    second.next = third

    llist.push(7)
    llist.push(34)
    llist.push(32)
    llist.push(21)

    llist.printList()
  #  llist.DeleteNode(34)
    #llist.DeleteNodeatPosition(2)
    print("checking after deleting")
    llist.printList()
