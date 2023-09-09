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

# Создаем словарь task_solvers, в котором будем хранить, сколько раз каждый студент решил каждую задачу
task_solvers = {}
for status in statuses:
    if status[4] == 'OK':
        key = (status[0], status[1])
        if key not in task_solvers:
            task_solvers[key] = set()
        task_solvers[key].add(status[2])

# Ищем студентов, которые решали задачу различными способами
multi_solvers = set()
for key, value in task_solvers.items():
    if len(value) > 1:
        multi_solvers.update(value)

# Для каждого статуса, у которого статус равен "OK" и идентификатор студента содержится в множестве multi_solvers,
# добав
