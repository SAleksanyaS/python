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


# Создаем словарь, где ключами являются названия групп, а значениями - количество сообщений
message_counts = {}
for message in messages:
    group = message[3]
    if group not in message_counts:
        message_counts[group] = 0
    message_counts[group] += 1

# Сортируем словарь по убыванию количества сообщений
sorted_message_counts = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)

# Создаем списки названий групп и количества сообщений в каждой группе
groups = [group for group, count in sorted_message_counts]
counts = [count for group, count in sorted_message_counts]

# Строим столбчатую диаграмму
plt.bar(groups, counts)
plt.title('Количество сообщений по группам')
plt.xlabel('Группы')
plt.ylabel('Количество сообщений')
plt.show()