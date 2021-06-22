class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, val):

        new_data = Node(val)
        new_data.next = self.head
        self.head = new_data

    def printList(self):

        tmp = self.head
        count = 0
        while tmp is not None:
            count += 1
            #print(tmp.data)
            tmp = tmp.next
        print(count)

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def getCountRec(self, node): #recursion
        if (not node):  # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    # def getCount(self):
    #     return self.getCountRec(self.head)

if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.push(45)
    llist.push(454)
    llist.push(4546)
    llist.push(45467)
    llist.push(454678)

    print(llist.getCount())