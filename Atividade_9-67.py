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

# 4. Plotagem dos gráficos SEPARADOS

# --- Gráfico 1: Aceleração Angular ---
plt.figure(figsize=(8, 6))
plt.plot(t, alpha, color='red', linewidth=2, label=r'$\alpha(t) = 2,40t$')
plt.ylabel(r'Acel. Angular $\alpha$ ($rad/s^2$)', fontsize=12)
plt.xlabel('Tempo (s)', fontsize=12)
plt.title('Aceleração Angular do Disco (9.67)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('./graficos/figure_9-67_aceleracao.png')
plt.close()

# --- Gráfico 2: Velocidade Angular ---
plt.figure(figsize=(8, 6))
plt.plot(t, omega, color='blue', linewidth=2, label=r'$\omega(t) = 1,20t^2$')
plt.ylabel(r'Vel. Angular $\omega$ ($rad/s$)', fontsize=12)
plt.xlabel('Tempo (s)', fontsize=12)
plt.title('Velocidade Angular do Disco (9.67)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Destacar o ponto de interesse (15 rad/s)
t_alvo = np.sqrt(15.0 / 1.20) 
plt.scatter([t_alvo], [15.0], color='black', zorder=5)
# Correção do SyntaxWarning: string raw (rf)
plt.annotate(rf't={t_alvo:.2f}s\n$\omega$=15 rad/s', xy=(t_alvo, 15), xytext=(t_alvo-1.5, 15), arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.savefig('./graficos/figure_9-67_velocidade.png')
plt.close()

# --- Gráfico 3: Posição Angular ---
plt.figure(figsize=(8, 6))
plt.plot(t, theta, color='green', linewidth=2, label=r'$\theta(t) = 0,40t^3$')
plt.ylabel(r'Posição Angular $\theta$ ($rad$)', fontsize=12)
plt.xlabel('Tempo (s)', fontsize=12)
plt.title('Posição Angular do Disco (9.67)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('./graficos/figure_9-67_posicao.png')
plt.close()