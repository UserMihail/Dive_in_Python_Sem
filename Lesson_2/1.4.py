"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

r = int(input('Введите радиус: '))

i = 2 * r * 3.14  # Длина окружности

s = 3.14 * r ** 2  # Площадь круга

print(f"Длина окружности: {i:.42f}, площадь круга: {s:.42f}")

