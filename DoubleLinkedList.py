class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList(object):

    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def remove(self, node):
         # if it's not the first element
        if node:
            if node.prev is not None:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
            else:
                # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                self.head = node.next
                node.next.prev = None

    def removeFirstNode(self):
        nodeData = self.head.data
        self.remove(self.head)
        return nodeData

    def search(self, node_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                return current_node

            current_node = current_node.next
        return None

    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            #print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            #print current_node.next.data if hasattr(current_node.next, "data") else None

            current_node = current_node.next
        print ''
        print "*"*50

'''
d = DoubleLinkedList()

n1=d.append(5)
n2=d.append(6)
n3=d.append(50)
n4=d.append(30)
#d.removeFirstNode()
d.show()
d.remove(n4)
#d.removeFirstNode()
node = d.append(17)
node = d.append(35)
d.remove(node)
d.show()

#d.remove(d.search(50))
#d.remove(d.search(5))
#d.removeFirstNode()

#d.show()

'''
