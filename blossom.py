from linked_list import Node, LinkedList
from flowers_lib import flower_definitions
class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(size)]

# Internal Methods
    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_key):
        return hash_key % self.array_size

# External Methods
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None

# Print Functions

    def print_hashmap(self):
        print("{hash_map:^36}".format(hash_map='Hash Map'))
        print(
            "{dash:-^36}\n{hash_title:>8} |{index_title:>9} | {key_title:<10}\n{dash:-^36}"
            .format(dash='-', hash_title='hash', index_title='index', key_title='key'))
        for item in flower_definitions:
            print("{hash:>8} | {index:>8} | {key:<15}".format(hash=self.hash(item[0]),index=self.compress(self.hash(item[0])),key=item[0]))
        print('\n')
    
    def print_hash_lists(self):
        print("{title:^55}".format(title="HashMap Collision Resolution using Separate Chaining"))
        print("{dash:-^55}".format(dash="-"))
        print("{key:<18} | {hash:<9} | {index:<9} | {value:<18}".format(key='Key', hash='Hash', index='Index', value='Value'))
        print("{dash:-^55}".format(dash="-"))
        for linklist in self.array:
            ll_head = linklist.get_head()
            if ll_head:
                current_node = ll_head.get_value()
                print("{key:<18} | {hash:<9} | {index:<9} | {value:<18}"
                .format(key=current_node[0], hash=self.hash(current_node[0]), index=self.compress(self.hash(current_node[0])), value=current_node[1]))
                for item in linklist:
                    current_item = item
                    if current_item != linklist.get_head().get_value():
                        print("\033[1;35;40m{key:<18} | {hash:<9} | {index:<9} | {value:<18}\033[m"
                        .format(key=current_item[0], hash=self.hash(current_item[0]), index=self.compress(self.hash(current_item[0])), value=current_item[1]))
        print("{dash:-^55}".format(dash="-"))

''' Test / Debug '''
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))

blossom.print_hashmap()
blossom.print_hash_lists()