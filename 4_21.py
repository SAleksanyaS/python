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
import random

# Создаем экземпляр HashTable и встроенного dict
ht = HashTable()
d = {}

# Записываем случайные значения в оба словаря
for i in range(10000):
    key = random.randint(0, 10000)
    value = random.randint(0, 10000)
    ht[key] = value
    d[key] = value

# Проверяем, что значения читаются корректно
for key in d.keys():
    assert ht[key] == d[key]

# Проверяем размеры словарей
assert len(ht) == len(d)
print("All tests passed!")

