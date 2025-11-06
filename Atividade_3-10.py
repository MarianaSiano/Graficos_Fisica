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

# c) Componente vertical ao atingir o solo
vy_final = g * t_total
print(f"Velocidade ao atingir o solo: vx = {v_x} m/s, vy = {vy_final:.2f} m/s")

# d) Diagramas
t = np.linspace(0, t_total, 500)
x_t = v_x * t
y_t = h - 0.5 * g * (t ** 2)
vx_t = np.full_like(t, v_x)
vy_t = -g * t

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t, x_t)
plt.title('x(t) - Posição horizontal')
plt.xlabel('Tempo (s)')
plt.ylabel('x (m)')

plt.subplot(2, 2, 2)
plt.plot(t, y_t)
plt.title('y(t) - Posição vertical')
plt.xlabel('Tempo (s)')
plt.ylabel('y (m)')

plt.subplot(2, 2, 3)
plt.plot(t, vx_t)
plt.title('vx(t) - Velocidade horizontal')
plt.xlabel('Tempo (s)')
plt.ylabel('vx (m/s)')

plt.subplot(2, 2, 4)
plt.plot(t, vy_t)
plt.title('vy(t) - Velocidade vertical')
plt.xlabel('Tempo (s)')
plt.ylabel('vy (m/s)')

plt.tight_layout()
plt.savefig('graficos.png')