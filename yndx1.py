import random
import string

# Генерация случайной строки
random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(2 * 10**5))

# Вывод строки
print(random_string)
