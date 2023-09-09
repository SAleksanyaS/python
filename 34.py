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

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

# О статусах см. https://github.com/kispython-ru/dta/blob/main/webapp/models.py#L44-L50



task_messages = {}

for message in messages:
    task = message[1]
    time = parse_time(message[4])
    week = time.isocalendar()[1] - 1  # Номер недели с начала семестра
    if task not in task_messages:
        task_messages[task] = [0] * 15  # 15 недель в семестре
    task_messages[task][week] += 1



for task, data in task_messages.items():
    plt.plot(range(len(data)), data, label=task)
plt.legend()
plt.xlabel('Неделя')
plt.ylabel('Количество сообщений')
plt.title('Изменение количества сообщений по задачам')
plt.show()
