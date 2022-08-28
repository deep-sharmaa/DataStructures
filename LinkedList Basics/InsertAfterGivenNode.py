
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertNode(self, afterNode, newNodee):
        nayaNode = Node(newNodee)
        nayaNode.next = afterNode.next
        afterNode.next = nayaNode
        return nayaNode


if __name__ == "__main__":

    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    print(ll.head.data)
    print(ll.head.next.data)
    print(second.next.data)

    newNode = 69
    after = second  # second node

    nayaNode = ll.insertNode(after, newNode)

    print(ll.head.data)
    print(ll.head.next.data)
    print(second.next.data)
    print(nayaNode.next.data)