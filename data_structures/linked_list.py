class Node(object):
    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):

        self.head = None
        self.size = 0

    def append(self, data):
            if not self.head:
                n = Node(data)
                self.head = n
                return
            else:
                n = self.head

                while n.next is not None:
                    n = n.next

                new_node = Node(data)
                n.next = new_node
                return 
                
    def is_empty(self):
        return not self.head

    def print_list(self):
        n = self.head

        while n:
            print str(n)
            n = n.next

ll = LinkedList()
elements = [1, 2, 3, 54, 6]
for element in elements:
    ll.append(element)

ll.print_list()