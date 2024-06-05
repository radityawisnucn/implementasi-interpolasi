import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    install('numpy')
    install('matplotlib')
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

# Pengujian fungsi interpolasi
test_points = [7, 12, 22, 28, 38]

print("Hasil Interpolasi Lagrange:")
for tp in test_points:
    print(f"x = {tp}, y = {interpolasi_lagrange(x_values, y_values, tp)}")

print("\nHasil Interpolasi Newton:")
for tp in test_points:
    print(f"x = {tp}, y = {interpolasi_newton(x_values, y_values, tp)}")

# Menghasilkan nilai untuk plot
x_plot = np.linspace(5, 40, 100)
y_plot_lagrange = [interpolasi_lagrange(x_values, y_values, xi) for xi in x_plot]
y_plot_newton = [interpolasi_newton(x_values, y_values, xi) for xi in x_plot]

# Membuat plot hasil interpolasi Lagrange
plt.plot(x_values, y_values, 'o', label='Titik Data')
plt.plot(x_plot, y_plot_lagrange, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Lagrange')
plt.grid(True)
plt.show()

# Membuat plot hasil interpolasi Newton
plt.plot(x_values, y_values, 'o', label='Titik Data')
plt.plot(x_plot, y_plot_newton, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Newton')
plt.grid(True)
plt.show()