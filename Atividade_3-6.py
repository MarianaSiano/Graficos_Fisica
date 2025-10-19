import matplotlib.pyplot as plt
import numpy as np

#--- Dados do Problema ---
#Vetor velocidade inicial v1 em t1 = 10.0s

v1_x = 2.6
v1_y = -1.8

#Vetor velocidade final v2 en t2 = 20.0s
v2_x = 6.4
v2_y = 0.5

#--- Configuração do Gráfico
#Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(8, 8))

#Desenha os vetores usando a função 'quiver'
ax.quiver(0, 0, v2_x, v2_y, angles='xy', scale_units='xy', scale=1, color='red',
        label=f'$\\vec{{v}}_2 = ({v2_x:.2f}\\hat{{i}}, {v2_y:.2f}\\hat{{j}})$ m/s')

#--- Estilização do Gráfico ---
#Define os limites dos eixos para melhor visualização
limite_x = max(abs(v1_x), abs(v2_x)) + 1
limite_y = max(abs(v1_y), abs(v2_y)) + 1
ax.set_xlim(-limite_x, limite_x)
ax.set_ylim(-limite_y, limite_y)

#Adiciona as linhas dos eixos x e y para referência
ax.axhline(0, color="black", linewidth=0.5)
ax.axhline(0, color="black", linewidth=0.5)

#Adiciona a grade
ax.grid(True, linestyle='--', alpha=0.6)

#Garante que a escala dos eixos seja a mesma (aspecto 1:1)
ax.set_aspect('equal', adjustable='box')

#Adiciona títulos e legendas
ax.set_title('Vetores Velocidade $\\vec{v}_1$ e $\\vec{v}_2$', fontsize=14)
ax.set_xlabel('Componente x da Velocidade ($v_x$) [m/s]', fontsize=12)
ax.set_ylabel('Componente y da Velocidade ($v_y$) [m/s]', fontsize=12)
ax.legend(fontsize=12)

#Mostra o gráfico
plt.show()