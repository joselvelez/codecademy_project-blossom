class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.linked_list = []

    def add_node(self, value):
        next_node = self.head
        node = Node(value, next_node)
        self.head = node
        self.linked_list.append(node)

    def remove_node(self, node):
        pass

    def get_head(self):
        return self.head

    def print_list(self):
        lst = []
        current_node = self.head
        lst.append(current_node.get_value())
        while current_node.get_next_node():
            lst.append(current_node.get_next_node().get_value())
            current_node = current_node.get_next_node()
        print(lst)

''' Test / Debug '''

test_node = Node('test1')
print("Node Value: {node}".format(node=test_node.get_value()))
print("Next Node: {next}".format(next=test_node.get_next_node()))

ll = LinkedList()
ll.add_node(1)
ll.add_node("two")
ll.add_node(3)
ll.add_node("four")
ll.add_node(5)
ll.add_node("six")
print("Current Head Node: {head}".format(head=ll.get_head().get_value()))
ll.print_list()