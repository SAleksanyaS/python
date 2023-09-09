from PIL import Image

def get_image_array(file_path):

    with Image.open(file_path) as img:
        # Получаем размеры изображения
        width, height = img.size
        # Создаем пустой массив нужного размера
        pixels = [[(0, 0, 0)] * height for i in range(width)]
        # Итерируемся по всем пикселям и заполняем массив значениями RGB
        for x in range(width):
            for y in range(height):
                pixels[x][y] = img.getpixel((x, y))
        return pixels


image_array = get_image_array('image.jpg')
print(image_array)
