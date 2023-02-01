from img_module import Image_Handler
import os

ob = Image_Handler()

hider = False

def show_menu():
    print("| МЕНЮ |")
    print("1) Загрузить файл\n2) Сохранить файл в JPG формате\n3) Сохранить файл в PNG формате\n4) Вывод информации о файле\n5) Показать изображение\n6) Список команд\n7) Выход")

show_menu()
while True:
    match input('-> '):
        case '1':
            path = input('Введите путь до файла => ')
            ob.set_pic(path)
        case '2':
            ob.save_jpg()
        case '3':
            ob.save_png()
        case '4':
            ob.pic_info()
        case '5':
            ob.show_pic()
        case '6':
            show_menu()
        case '7':
            break
        case _:
            print('Неправильный номер команды!')