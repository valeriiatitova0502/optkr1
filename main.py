import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x):
    return np.where(x != 0, 2 * x**2 + 16 / x, np.nan)  # Используем np.nan для точек x=0

# Метод золотого сечения
def golden_search(f, a, b, tol):
    iterations = 0
    golden_ratio = (1 + np.sqrt(5)) / 2

    print("Итерация\tЛевая граница\tПравая граница\tКорень\t\tf(x)")

    while abs(b - a) > tol:
        x1 = b - (b - a) / golden_ratio
        x2 = a + (b - a) / golden_ratio

        f_x1 = f(x1)
        f_x2 = f(x2)

        if f_x1 < f_x2:
            b = x2
        else:
            a = x1

        print(f"{iterations}\t\t{a:.6f}\t\t{b:.6f}\t\t{(a + b) / 2:.6f}\t\t{f((a + b) / 2):.6f}")
        iterations += 1

    return (a + b) / 2, f((a + b) / 2)

# Интервал для поиска экстремума
a_left1, b_left1 = -1, -0.000001
a_left2, b_left2 = 0.000001, 5

# Точность поиска
tolerance = 1e-6

# Использование метода золотого сечения для интервала [-1, -0.000001]
root_golden_left1, extremum_value_golden_left1 = golden_search(f, a_left1, b_left1, tolerance)
print(f'\nЭкстремум функции f(x) на интервале [-1, -0.000001] методом золотого сечения находится в точке {root_golden_left1:.6f} с f(x) = {extremum_value_golden_left1:.6f}')

# Использование метода золотого сечения для интервала [0.000001, 5]
root_golden_left2, extremum_value_golden_left2 = golden_search(f, a_left2, b_left2, tolerance)
print(f'\nЭкстремум функции f(x) на интервале [0.000001, 5] методом золотого сечения находится в точке {root_golden_left2:.6f} с f(x) = {extremum_value_golden_left2:.6f}')

# Построение графика функции для обоих интервалов
x_values_left1 = np.linspace(a_left1, b_left1, 1000, endpoint=False)
y_values_left1 = f(x_values_left1)

x_values_left2 = np.linspace(a_left2, b_left2, 1000)
y_values_left2 = f(x_values_left2)

plt.figure(figsize=(8, 6))

# График для интервала [-1, -0.000001]
plt.plot(x_values_left1, y_values_left1, label='f(x) = 2x^2 + 16/x', color='b')
plt.scatter(root_golden_left1, extremum_value_golden_left1, color='m', marker='o', label=f'Золотое сечение (-1, -0.000001) ({root_golden_left1:.6f}, {extremum_value_golden_left1:.6f})')

# График для интервала [0.000001, 5]
plt.plot(x_values_left2, y_values_left2, label='f(x) = 2x^2 + 16/x', color='g')
plt.scatter(root_golden_left2, extremum_value_golden_left2, color='r', marker='o', label=f'Золотое сечение (0.000001, 5) ({root_golden_left2:.6f}, {extremum_value_golden_left2:.6f})')

plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.grid()
plt.xlabel('x')
plt.title('График функции для обоих интервалов')
plt.legend()
plt.show()
