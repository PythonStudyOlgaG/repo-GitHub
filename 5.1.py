"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
#input_txt = input("Введите текст:")
def file_input():
    """Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка."""
    with open("somefile.txt", "w+") as mf:
        while True:
            input_s = input()
            if input_s == " ": break
            mf.write(input_s + "\n")
    #mf.close() - не требуется, поскольку использована инструкция with, которая автоматически закроет файл

go = file_input()