class HashTable:
    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        hash_key = hash(key) % self.size
        for i, item in enumerate(self.data[hash_key]):
            if item[0] == key:
                self.data[hash_key][i] = (key, value)
                return
        self.data[hash_key].append((key, value))

    def __getitem__(self, key):
        hash_key = hash(key) % self.size
        for item in self.data[hash_key]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __len__(self):
        return sum(len(bucket) for bucket in self.data)

    def __iter__(self):
        return Iterator(self.data, self.size)

class Iterator:
    def __init__(self, data, size):
        self.data = data
        self.size = size
        self.current_bucket = 0
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_bucket < self.size:
            if self.current_item < len(self.data[self.current_bucket]):
                item = self.data[self.current_bucket][self.current_item]
                self.current_item += 1
                return item
            else:
                self.current_bucket += 1
                self.current_item = 0
        raise StopIteration()
ht = HashTable()

ht[1] = 'one'
ht[2] = 'two'
ht[3] = 'three'

for key, value in ht:
    print(key, value)
