# TIFF to JPG

## Установка библиотеки Pillow
```
p+ip install pillow==9.5.0
```
## Импортируем библиотеки

```python
import os
from PIL import Image
```
## Функция

```python
def tif_to_jpg(input_folder, output_folder):
    if os.path.exists(input_folder) == False or os.path.isdir(input_folder) == False:
        return f'Incorrect path: {input_folder}'
    
    if os.path.exists(output_folder) == False or os.path.isdir(output_folder) == False:
        return f'Incorrect path: {output_folder}'

    loaded = 0
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.tif') or file_name.endswith('.tiff'):
            try:
                img = Image.open(os.path.join(input_folder, file_name))
                new_file_name = os.path.splitext(file_name)[0] + '.jpg'
                output_path = os.path.join(output_folder, new_file_name)
                img.save(output_path, 'JPEG')
                loaded += 1
                print(f"loaded: {new_file_name}")
            except Exception as e:
                return e
        
    return f'Загружено файлов: {loaded}'

if __name__ == '__main__':
    paths = input('From/To:').strip().split()
    print(tif_to_jpg(paths[0], paths[1]))
```

## Проверка, существует ли нужный нам путь

```python
if os.path.exists(input_folder) == False or os.path.isdir(input_folder) == False:
        return f'Incorrect path: {input_folder}'
    
    if os.path.exists(output_folder) == False or os.path.isdir(output_folder) == False:
        return f'Incorrect path: {output_folder}'
```
## Перебор всех файлов, если они с расширением .tif, сохраняем с новым расширением .jpg по новому пути

```python
loaded = 0
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.tif') or file_name.endswith('.tiff'):
            try:
                img = Image.open(os.path.join(input_folder, file_name))
                new_file_name = os.path.splitext(file_name)[0] + '.jpg'
                output_path = os.path.join(output_folder, new_file_name)
                img.save(output_path, 'JPEG')
                loaded += 1
                print(f"loaded: {new_file_name}")
            except Exception as e:
                return e
```
## Запрос путей и вызов функции

```python
if __name__ == '__main__':
    paths = input('From/To:').strip().split()
    print(tif_to_jpg(paths[0], paths[1]))
```
