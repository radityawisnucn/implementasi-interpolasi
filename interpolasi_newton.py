import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_values = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_values = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def interpolasi_newton(x_points, y_points, x):
    n = len(x_points)
    coef = np.zeros([n, n])
    coef[:, 0] = y_points

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_points[i + j] - x_points[i])

    def newton_poly(coef, x_points, x):
        n = len(x_points) - 1
        p = coef[n]
        for k in range(1, n + 1):
            p = coef[n - k] + (x - x_points[n - k]) * p
        return p

    return newton_poly(coef, x_points, x)

# Menghasilkan nilai untuk plot
x_plot = np.linspace(5, 40, 100)
y_plot = [interpolasi_newton(x_values, y_values, xi) for xi in x_plot]

# Membuat plot hasil interpolasi
plt.plot(x_values, y_values, 'o', label='Titik Data')
plt.plot(x_plot, y_plot, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Newton')
plt.grid(True)
plt.show()
