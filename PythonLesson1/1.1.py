"""
1. Поработайте с переменными,
(1)создайте несколько,
(2)выведите на экран,
(3)запросите у пользователя несколько чисел и строк и сохраните в переменные,
(4)выведите на экран.
"""
# (1) Создаю несколько переменных
variance_list = ["Это список, если начинается с квадратной скобочки [", 1, "january", 2021, 01.01, None]
variance_tuple = ("Это кортеж, если начинается с круглой скобочки (", 2, 5.30, None)
variance_dict = {"Это словарь, если начинается с фигурной скобочки {": "{", "A это переменная типа NonType": None}

# (2) Вывожу переменные на экран
print(
    "Список это изменяемая упорядоченная коллекция объектов произвольных типов, например: \n",
    variance_list, type(variance_list),
    "\nКортеж это неизменяемая упорядоченная коллекция объектов произвольных типов, например: \n",
    variance_tuple, type(variance_tuple),
    "\nСловарь это неупорядоченная коллекция произвольных объектов с доступом по ключу, например: \n",
    variance_dict, type(variance_dict)
     )

# (3) Запрашиваю у пользователя несколько чисел и строк и сохраняю в переменные
# Далее на примере переменной any_type_input_variance для собственного понимания использую динамическую типизацию
# Динамическая типизация - тип переменной определяется автоматически во время использования,
# Фактически, переменная any_type_input_variance работает, как своего рода гиперссылка

any_type_input_variance = int(input("Введите целое число: "))
print("Вы ввели целое число: ", any_type_input_variance, type(any_type_input_variance))
variance_int = any_type_input_variance
any_type_input_variance = float(input("Введите дробное число (число с плавающей точкой): "))
variance_float = any_type_input_variance
print("Вы ввели дробное число (число с плавающей точкой): ", any_type_input_variance, type(any_type_input_variance))
any_type_input_variance = input("Введите строку или слово: ")
variance_str = any_type_input_variance
print("Вы ввели строку или слово: ", any_type_input_variance, type(any_type_input_variance))

# (4) Вывожу на экран
print("\nЗначение переменной any_type_input_variance: ", any_type_input_variance, type(any_type_input_variance),
      "\nВы ввели целое число: ", variance_int, type(variance_int),
      "\nВы ввели дробное число (число с плавающей точкой): ", variance_float, type(variance_float),
      "\nВы ввели строку или слово: ", variance_str, type(variance_str)
     )



