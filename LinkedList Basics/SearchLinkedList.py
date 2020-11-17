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

    def SearchKey(self, key):

        tmp = self.head
        if tmp is None:
            return "Head is empty"

        if tmp.data == key:
            return "Value found at HEAD"

        count = 1
        while tmp:
            if tmp.data == key:
                return "Value Found at"+" "+str(count)
            tmp = tmp.next
            count+=1

    def getSearchValue(self, node, key):

        print(node)
        print(key)
        if node:
            if node.data == key:
                return True
            else:
                return self.getSearchValue(node.next, key)
        else:
            return self.getSearchValue(node.next, key)

if __name__ == '__main__':

    llist = LinkedList()

    llist.push(45)
    llist.push(454)
    llist.push(4546)
    llist.push(45467)
    llist.push(454678)

    print(llist.getSearchValue(llist.head, 454))