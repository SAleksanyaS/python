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

    def __delitem__(self, key):
        hash_key = hash(key) % self.size
        for i, item in enumerate(self.data[hash_key]):
            if item[0] == key:
                del self.data[hash_key][i]
                return
        raise KeyError(key)

    def __contains__(self, key):
        hash_key = hash(key) % self.size
        for item in self.data[hash_key]:
            if item[0] == key:
                return True
        return False

    def keys(self):
        return [item[0] for bucket in self.data for item in bucket]

    def values(self):
        return [item[1] for bucket in self.data for item in bucket]

    def items(self):
        return [(item[0], item[1]) for bucket in self.data for item in bucket]

    def get(self, key, default=None):
        hash_key = hash(key) % self.size
        for item in self.data[hash_key]:
            if item[0] == key:
                return item[1]
        return default

    def pop(self, key, default=None):
        hash_key = hash(key) % self.size
        for i, item in enumerate(self.data[hash_key]):
            if item[0] == key:
                del self.data[hash_key][i]
                return item[1]
        if default is not None:
            return default
        raise KeyError(key)

    def clear(self):
        self.data = [[] for _ in range(self.size)]

    def update(self, other):
        for key, value in other.items():
            self[key] = value

    def __len__(self):
        return sum(len(bucket) for bucket in self.data)

    def __iter__(self):
        return iter(self.keys())

    def __str__(self):
        return str(dict(self.items()))

    def __repr__(self):
        return str(self)
