class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):

        node = self.head
        while node:
            print(node.data)
            node = node.next


    def push(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Function to swap Nodes x and y in linked list by
    # changing links
    def swapNodes(self, x, y):

        # Nothing to do if x and y are same
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def swapNodesOptimized(self, x, y):
        head = self.head

        # Nothing to do if x and y are same
        if (x == y):
            return None

        a = None
        b = None

        # search for x and y in the linked list
        # and store therir pointer in a and b
        while (self.head.next != None):

            if ((self.head.next).data == x):
                a = self.head

            elif ((self.head.next).data == y):
                b = self.head

            self.head = ((self.head).next)

        # if we have found both a and b
        # in the linked list swap current
        # pointer and next pointer of these
        if (a != None and b != None):
            temp = a.next
            a.next = b.next
            b.next = temp
            temp = a.next.next
            a.next.next = b.next.next
            b.next.next = temp




if __name__ == '__main__':

     llist = LinkedList()
     llist.head = Node(10)
     llist.push(15)
     llist.push(12)
     llist.push(13)
     llist.push(20)
     llist.push(14)

     llist.printList()
     llist.swapNodesOptimized(10,20)
     print("-"*20)
     llist.printList()


