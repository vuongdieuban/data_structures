"""
WRITING LINKED LIST FROM SCRATCH
"""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


class UnorderedList(Node):
    """"
    functions:
        def insertAtEnd(): add item to the end of the list, similar to append
        def insertAtBeginning(): add item to the beginning of the list
        def pop(): remove at the end node (last in first out)
        def print() : traverse the list and print data at every node
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insertAtEnd(self, item):
        last_node = self.head   # since we cannnot modify the head, we use the last_node to traverse the list
        new_node = Node(item)
        new_node.data = item
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        if self.head is not None:
            while last_node.next is not None:   # use last_node to traverse the list and link to new node
                last_node = last_node.next
            last_node.next = new_node
            return

    def insertAtBeginning(self, item):
        new_node = Node(item)
        new_node.data = item

        if self.head is None:
            new_node.next = None
            self.head = new_node
            return

        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
            return

    def print(self):
        temp = self.head
        print("List is:")
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.insertAtEnd(5)
    mylist.insertAtEnd(7)
    mylist.insertAtEnd(10)
    mylist.insertAtEnd(11)
    mylist.insertAtBeginning(8)
    mylist.insertAtBeginning(2)
    mylist.print()
