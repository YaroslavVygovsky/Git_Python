import math
b =float(input('Введите сторону равностороннего треугольника: '));
r =float(input('Введите радиус круга= '));
if r==(b*math.sqrt(3)/6):
    print('Существует')
else:
    print('Не существует')
