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
    def __init__(self, value=None):
        self.value = value
        self.head = None

    def add_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def remove_node(self, value_to_remove):
        current_node = self.head
        if current_node.get_value() == value_to_remove:
            self.head = current_node.get_next_node()
        else:
            while current_node:
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node = current_node.set_next_node(current_node.get_next_node().get_next_node())
                else:
                    current_node = current_node.get_next_node()

    def get_head(self):
        return self.head

    def print_list(self):
        str_lst = ""
        current_node = self.get_head()
        while current_node:
            if current_node.get_value() != None:
                str_lst += str(current_node.get_value()) + " --> "
            current_node = current_node.get_next_node()
        print(str_lst)

''' Test / Debug '''

# test_node = Node('test1')
# print("Node Value: {node}".format(node=test_node.get_value()))
# print("Next Node: {next}".format(next=test_node.get_next_node()))

ll = LinkedList()
ll.add_beginning(1)
ll.add_beginning("two")
ll.add_beginning(3)
ll.add_beginning("four")
ll.add_beginning(5)
ll.add_beginning("six")
ll.add_beginning(7)
ll.remove_node(3)
print("Current Head Node: {head}".format(head=ll.get_head().get_value()))
ll.print_list()