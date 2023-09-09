import csv
import datetime
from collections import defaultdict

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



task_counts = defaultdict(lambda: {'total': 0, 'correct': 0})

for row in statuses:
    task_counts[row[0]]['total'] += 1
    if row[4] == '2':
        task_counts[row[0]]['correct'] += 1


for task, counts in task_counts.items():
    counts['percent_correct'] = counts['correct'] / counts['total'] * 100

# топ  легких
easiest_tasks = sorted(task_counts.items(), key=lambda x: x[1]['percent_correct'], reverse=True)[:7]

# топ  сложных
hardest_tasks = sorted(task_counts.items(), key=lambda x: x[1]['percent_correct'])[:7]


labels, values = zip(*[(task, counts['percent_correct']) for task, counts in easiest_tasks])
plt.bar(labels, values)
plt.title('топ легких')
plt.show()