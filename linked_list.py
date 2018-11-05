"""
WRITING LINKED LIST FROM SCRATCH
"""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


class UnorderedList():
    """"
    functions:
        def insertAtEnd(self, item): add item to the end of the list, similar to append
        def insertAtBeginning(self, item): add item to the beginning of the list
        def insertAtPos(self, item, pos): add item at any position pos, first position in list is pos = 1
        def removeAtPos(self, item, pos): remove item at any position pos, first position in list is pos = 1
        def reverseList(self, temp): reverse the linked list using recursion

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

        while last_node.next is not None:   # use last_node to traverse the list and link to new node
            last_node = last_node.next
        last_node.next = new_node
        return

    def insertAtBeginning(self, item):
        new_node = Node(item)
        new_node.data = item

        new_node.next = self.head   # head is init as None, so if list is empty, first node.next = None
        self.head = new_node
        return

    def insertAtPos(self, item, pos):
        new_node = Node(item)
        new_node.data = item
        new_node.next = None

        if pos == 1:    # handle empty list, add item at beginning, pos == 1, acts as insertAtBeginning
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return

    def removeAtPos(self,pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        delete_node = temp.next
        temp.next = delete_node.next
        return

    def reverseList(self, temp):
        if temp.next is None:
            self.head = temp
            return

        self.reverseList(temp.next)
        temp.next.next = temp
        temp.next = None

    def print(self):
        temp = self.head
        print("List is:")
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.insertAtEnd(5)   # 5
    mylist.insertAtEnd(7)   # 5, 7
    mylist.insertAtBeginning(8) # 8, 5, 7,
    mylist.insertAtBeginning(2) # 2, 8, 5, 7,
    mylist.insertAtPos(3, 2) # 2, 3, 8, 5, 7,
    mylist.insertAtPos(5, 1) # 5, 2, 3, 8, 5, 7
    mylist.removeAtPos(4)  # 5, 2, 3, 5, 7
    mylist.removeAtPos(1) # 2, 3, 5, 7
    mylist.reverseList(mylist.head) # 7, 5, 3, 2

    mylist.print()
