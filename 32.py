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


hours = [parse_time(msg[4]).hour for msg in messages]

plt.hist(hours, bins=24)
plt.title('Распределение активности студентов по времени суток')
plt.xlabel('Часы')
plt.ylabel('Число сообщений')
plt.show()