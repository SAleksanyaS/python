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


# Создаем словарь, где ключами являются названия групп, а значениями - количество ачивок
achiv_counts = {}
for statuses in statuses:
    var = statuses[1]
    if var not in achiv_counts:
        achiv_counts[var] = 0
    achiv_counts[var] += 1

# Сортируем словарь по убыванию количества сообщений
sorted_message_counts = sorted(achiv_counts.items(), key=lambda x: x[1], reverse=True)

# Создаем списки названий групп и количества ачивок в каждой группе
var = [var for var, count in sorted_message_counts]
counts = [count for var, count in sorted_message_counts]

# Строим столбчатую диаграмму
plt.bar(var, counts)
plt.title('ачивки')
plt.xlabel('Группы')
plt.ylabel('Количество ачивок')
plt.show()