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


weekday_counts = [0] * 7
for row in messages:
    time = parse_time(row[4])
    weekday_counts[time.weekday()] += 1


plt.bar(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], weekday_counts)
plt.title('Student activity by day of the week (messages.csv)')
plt.xlabel('Day of the week')
plt.ylabel('Number of records')
plt.show()