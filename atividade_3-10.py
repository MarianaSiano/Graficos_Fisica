import numpy as np
import matplotlib.pyplot as plt

g = 9.8 # Gravidade (m/s^2)
h = 300 # Altura inicial (m)
v_x = 60 # Velocidade horizontal (m/s)

# a) Tempo para atingir o solo
t_total = np.sqrt((2 * h) / g)
print(f"Tempo para atingir o solo: {t_total: .2f} s")

# b) Distância horizontal
x_total = v_x * t_total
print(f"Distância horizontal: {x_total: .2f} m")