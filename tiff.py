import os
from PIL import Image

def tif_to_jpg(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.tif'):
            # Создайте объект изображения
            img = Image.open(os.path.join(input_folder, file_name))

            # Создайте путь к новому файлу JPEG
            new_file_name = os.path.splitext(file_name)[0] + '.jpg'
            output_path = os.path.join(output_folder, new_file_name)

            # Сохраните изображение в формате JPEG
            img.save(output_path, 'JPEG')

if __name__ == '__main__':
    tif_to_jpg('./folder_input', './folder_output')