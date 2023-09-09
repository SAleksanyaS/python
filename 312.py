import csv
import datetime
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# Загрузка данных из CSV-файла
baza = load_csv('baza.csv')

# Создание словаря для хранения количества игр каждого жанра для каждого года
genres_by_year = {}

# Подсчет количества игр каждого жанра для каждого года
for row in baza:
    year = row[3]
    genre = row[1]
    if year not in genres_by_year:
        genres_by_year[year] = {}
    if genre not in genres_by_year[year]:
        genres_by_year[year][genre] = 0
    genres_by_year[year][genre] += 1

# Визуализация данных в виде графиков
for genre in genres_by_year['2000']:
    years = list(genres_by_year.keys())
    counts = [genres_by_year[year][genre] if genre in genres_by_year[year] else 0 for year in years]
    plt.plot(years, counts, label=genre)

plt.xlabel('Год')
plt.ylabel('Количество игр')
plt.title('Популярность жанров в различные периоды времени')
plt.legend()
plt.show()
