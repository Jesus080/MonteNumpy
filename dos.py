import numpy as np
import matplotlib.pyplot as plt

def estimate_pi_numpy(num_samples):
    # Generar puntos aleatorios en el cuadrado [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    # Calcular la distancia desde el origen
    distance = x**2 + y**2

    # Contar cuántos puntos caen dentro del círculo de radio 1
    inside_circle = np.sum(distance <= 1)

    # Estimar pi
    pi_estimate = (inside_circle / num_samples) * 4

    return pi_estimate, x, y, distance <= 1

# Número de muestras para la simulación
num_samples = 100000

# Estimar el valor de pi
pi_estimate, x, y, inside_circle = estimate_pi_numpy(num_samples)

# Mostrar el resultado
print(f"Estimación de pi: {pi_estimate}")

# Visualización de la simulación
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color="blue", marker=".", label="Dentro del círculo")
plt.scatter(x[~inside_circle], y[~inside_circle], color="red", marker=".", label="Fuera del círculo")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Estimación de Pi usando Monte Carlo con {num_samples} muestras\nEstimación: {pi_estimate}")
plt.legend()
plt.show()
