from PIL import Image
import os

DIR = os.path.abspath(os.getcwd())


class Image_Handler:
    def __init__(self):
        self.pic = None

    def set_pic(self, path):
        try:
            self.pic = Image.open(path)
        except FileNotFoundError:
            print("Файл не найден!")

    def save_jpg(self):
        if self.pic is not None:
            # unique pic
            self.pic.save(f"{DIR}/res/smth.jpg", format="JPEG")
        else:
            print("Не было загружено изображение!")
    # информация о изображении

img_path = input()
img_obj = Image_Handler()
img_obj.save_jpg()
img_obj.set_pic(img_path)
img_obj.save_jpg()
