from PIL import Image, UnidentifiedImageError
import os

DIR = os.path.abspath(os.getcwd())

class Image_Handler:
    def __init__(self):
        self.pic = None

    def set_pic(self, path):
        try:
            # проверка на форматы
            self.pic = Image.open(path)
        except FileNotFoundError:
            print("Файл не найден!")
        except UnidentifiedImageError:
            print("Файл не может быть открыт или идентифицирован!")
        except:
            print("Неизвестная ошибка!")

    def save_jpg(self):
        if self.pic is not None:
            # unique pic name
            # ошибки
            self.pic.save(f"{DIR}/res/smth.jpg", format="JPEG")
        else:
            print("Не было загружено изображение!")
    
    def pic_info(self):
        if self.pic is not None:
            print("[Данные изображения]")
            print(f"Формат -> {self.pic.format}")
            print(f"Размер -> {self.pic.size}")
        else:
            print("Не было загружено изображение!")
