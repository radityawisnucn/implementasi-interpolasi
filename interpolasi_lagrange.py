import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_values = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_values = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def interpolasi_lagrange(x_points, y_points, x):
    def L(k, x):
        Lk = 1
        for i in range(len(x_points)):
            if i != k:
                Lk *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return Lk

    y = 0
    for k in range(len(y_points)):
        y += y_points[k] * L(k, x)
    return y

# Menghasilkan nilai untuk plot
x_plot = np.linspace(5, 40, 100)
y_plot = [interpolasi_lagrange(x_values, y_values, xi) for xi in x_plot]

# Membuat plot hasil interpolasi
plt.plot(x_values, y_values, 'o', label='Titik Data')
plt.plot(x_plot, y_plot, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Lagrange')
plt.grid(True)
plt.show()
