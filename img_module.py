from PIL import Image, UnidentifiedImageError
import os
from datetime import datetime

DIR = os.path.abspath(os.getcwd())

class Image_Handler:
    def __init__(self):
        self.pic = None

    def set_pic(self, path):
        try:
            # проверка на форматы + брать имя файла
            self.pic = Image.open(path)
        except FileNotFoundError:
            print("Файл не найден!")
        except UnidentifiedImageError:
            print("Файл не может быть открыт или идентифицирован!")
        except:
            print("Неизвестная ошибка!")

    def save_jpg(self):
        if self.pic is not None:
            # добавить в имя файла его предыдущее имя
            # ошибки
            self.pic.save(f'{DIR}/res/{datetime.now().strftime("%H-%M-%S")}.jpg', format="JPEG")
        else:
            print("Изображение не было загружено!")
    
    def save_png(self):
        if self.pic is not None:
            self.pic.save(f'{DIR}/res/{datetime.now().strftime("%H-%M-%S")}.png', format="PNG")
        else:
            print("Изображение не было загружено!")

    def pic_info(self):
        if self.pic is not None:
            print("[Данные изображения]")
            print(f"Формат -> {self.pic.format}")
            print(f"Размер -> {self.pic.size}")
        else:
            print("Изображение не было загружено!")

    def show_pic(self):
        if self.pic is not None:
            self.pic.show()
        else:
            print("Изображение не было загружено!")
