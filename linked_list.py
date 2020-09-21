class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        current_node = self.head

        if not current_node:
            self.head = new_node
            print("Added {node_added} to the LinkedList for the key {key}.\n \033[1;32;40m This is the first element in the list with this key.\n \033[m"
            .format(node_added=new_node.get_value(), key=new_node.get_value()[0]))

        while current_node:
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
                print("Added {node_added} to the LinkedList for the key {key}.\n \033[1;35;40m There are elements already in this list. The new element has been appended to the end.\n \033[m"
                .format(node_added=new_node.get_value(), key=new_node.get_value()[0]))
            current_node = next_node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_next_node()

    def remove_node(self, value_to_remove):
        current_node = self.head
        if current_node.get_value() == value_to_remove.get_value():
            self.head = current_node.get_next_node()
        else:
            while current_node:
                if current_node.get_next_node().get_value() == value_to_remove.get_value():
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
# ll = LinkedList()
# one = Node([1,'one'])
# ll.insert(one)
# two = Node([2, "two"])
# ll.insert(two)
# three = Node([3, 'three'])
# ll.insert(three)
# four = Node([4, "four"])
# ll.insert(four)
# five = Node([5, 'five'])
# ll.insert(five)
# six = Node([6, "six"])
# ll.insert(six)
# seven = Node([7, 'seven'])
# ll.insert(seven)
# ll.remove_node(three)
# print("Current Head Node: {head}".format(head=ll.get_head().get_value()))
# ll.print_list()