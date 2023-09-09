import numpy as np
from PIL import Image
from scipy.spatial import Voronoi, voronoi_plot_2d

# Загрузка изображения
image = Image.open("image.jpg")
pixels = np.array(image)

# Генерация случайных точек
num_points = 2000
points = np.random.randint(0, pixels.shape[0], size=(num_points, 2))

# Вычисление диаграммы Вороного
vor = Voronoi(points)

# Формирование массива с цветами пикселей
result = np.zeros_like(pixels)
for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        distances = np.sqrt(np.sum((points - [i, j])**2, axis=1))
        index = np.argmin(distances)
        result[i, j] = pixels[points[index][0], points[index][1]]

# Сохранение результата
result_image = Image.fromarray(result)
result_image.save("save1.jpg")
