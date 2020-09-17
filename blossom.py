

class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [None for item in range(self.size)]

# Internal Methods

    def hash(self, key):
        hash_key = sum(key.encode())
        return hash_key

    def compressor(self, key):
        index = self.hash(key) % self.size
        return index

# External Methods

    def assign(self, key, value):
        self.array[self.compressor(key)] = [key, value]
        print("Added {key} corresponding to {value} to the HashMap.".format(key=key, value=value))

    def retrieve(self, key):
        array_index = self.compressor(key)
        payload = self.array[array_index]
        if payload != None:
            if payload[0] != key:
                return None
            else:
                return payload
        else:
            return None

    def print_hashmap(self):
        for item in self.array:
            if item is None:
                print(self.array)
            else:
                print('Index {index}: Key: {key} Value: {value}'.format(index=self.array.index(item), key=item[0], value=item[1]))

''' Test / Debug '''

blossom_hashmap = HashMap(20)
print(blossom_hashmap.hash('jose'))
print(blossom_hashmap.compressor('jose'))
blossom_hashmap.assign("jose","human")

#blossom_hashmap.print_hashmap()

print(blossom_hashmap.retrieve("jose"))
