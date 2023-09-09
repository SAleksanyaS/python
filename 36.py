import csv
import datetime
from collections import Counter
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


correct_counts = Counter()

for row in statuses:
    if row[4] == '2':
        correct_counts[row[2]] += 1

top_groups = correct_counts.most_common(5)

labels, values = zip(*top_groups)
plt.bar(labels, values)
plt.title('топ 5 групп')
plt.show()