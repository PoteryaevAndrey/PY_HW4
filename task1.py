# Вычислить число c заданной точностью 


from cmath import pi

d = int(input('Введите точность числа Пи '))
print(f'Число Пи с заданной точностью {d} равно {round(pi,d)}')