import numpy as np
import matplotlib.pyplot as plt

# 1. Definição dos parâmetros físicos
R = 0.25 # Raio do disco em metros (25cm)
A = 0.60 # Constante calculada no item (a)

# 2. Criação do vetor
# Simular de 0 a 4 s para cobrir o instante de interesse (aprox. 3.54s)
t = np.linspace(0, 4, 200)

# 3. Equações do movimento (Escritas explicitamente)

# Aceleração angular: alpha(t) = 2.40t
# (Derivado de: alpha = At/R = 0.60t/0.25)
alpha = 2.40 * t

# Velocidade angular: omega(t) = 1.20t^2
# (Derivado de: integral de 2.40t)
omega = 1.20 * t ** 2

# Posição angular: theta(t) = 0.40t^3
# (Derivado de: integral de 1.20t^2)
theta = 0.40 * t ** 3

# 4. Plotagem dos gráficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Gráfico da Aceleração Angular
ax1.plot(t, alpha, color='red', linewidth=2, label=r'$\alpha(t) = 2,40t$')
ax1.set_ylabel(r'Acel. Angular $\alpha$ ($rad/s^2$)', fontsize=12)
ax1.set_title('Cinemática Rotacional do Disco (Problema 9.67)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Gráfico da Velocidade Angular
ax2.plot(t, omega, color='blue', linewidth=2, label=r'$\omega(t) = 1,20t^2$')
ax2.set_ylabel(r'Vel. Angular $\omega$ ($rad/s$)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

# Destacar o ponto de interesse (15 rad/s)
t_alvo = np.sqrt(15.0 / 1.20) # t aprox 3.54s
ax2.scatter([t_alvo], [15.0], color='black', zorder=5)

# Adicionado 'r' antes do f-string para corrigir o erro de sintaxe do \omega
ax2.annotate(rf't={t_alvo:.2f}s\n$\omega$=15 rad/s', xy=(t_alvo, 15), xytext=(t_alvo-1.5, 15), arrowprops=dict(facecolor='black', shrink=0.05))

# Gráfico da Posição Angular
ax3.plot(t, theta, color='green', linewidth=2, label=r'$\theta(t) = 0,40t^3$')
ax3.set_ylabel(r'Posição Angular $\theta$ ($rad$)', fontsize=12)
ax3.set_xlabel('Tempo (s)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.legend()

plt.tight_layout()
plt.savefig('./graficos/figure_9-67.png')