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

# name, genre, html page, status
baza = load_csv('baza.csv')

# Создаем словарь, где ключами являются дата выхода, а значениями - количество выпущенных игр
years_counts = {}
for baza in baza:
    group = baza[3]
    if group not in years_counts:
        years_counts[group] = 0
    years_counts[group] += 1



sorted_message_counts = sorted(years_counts.items(), key=lambda x: x[1], reverse=True)

groups = [group for group, count in sorted_message_counts]
counts = [count for group, count in sorted_message_counts]

# Строим столбчатую диаграмму
plt.bar(groups, counts)
plt.title('Количество выпущенных игр по годам')
plt.xlabel('годы')
plt.ylabel('Количество выпущенных игр')
plt.show()