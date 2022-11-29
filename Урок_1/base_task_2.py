"""
Базовое задание #2
Пользователь вводит время в секундах. Переведите время в часы, минуты
и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
input_seconds = int(input("Введите время (сек): "))
seconds = input_seconds % 60
hours = input_seconds // 3600
minutes = (input_seconds // 60) % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
