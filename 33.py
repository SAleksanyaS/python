import csv
import datetime
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv('messages.csv')

# id, message_id, time, status
checks = load_csv('checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')


# Создание словаря для хранения количества сообщений по каждой задаче
message_counts = {}

# Перебор всех сообщений и подсчет количества сообщений по каждой задаче
for row in messages:
    task = row[1]
    if task not in message_counts:
        message_counts[task] = 1
    else:
        message_counts[task] += 1


values = list(message_counts.values())

# Создание гистограммы
plt.bar(['0', '1', '2', '3', '4', '5', '6', '7'], values)
plt.title('Распределение активности студентов по задачам')
plt.xlabel('Задачи')
plt.ylabel('Число решений')
plt.show()