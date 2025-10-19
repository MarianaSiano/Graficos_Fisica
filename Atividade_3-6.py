import matplotlib.pyplot as plt
import numpy as np

#--- Dados do Problema ---
#Vetor velocidade inicial v1 em t1 = 10.0s

v1_x = 2.6
v1_y = -1.8

#Vetor velocidade final v2 en t2 = 20.0s
v2_x = 6.40
v2_y = 0.50

#--- Configuração do Gráfico ---
#Cria a figura e os eixos onde o gráfico será desenhado
fig, ax = plt.subplots(figsize=(10, 8)) # Ajustado para melhor visualização

#--- Desenho dos Vetores ---
#Desenha o vetor v1 (azul) partindo da origem (0,0)
ax.quiver(0, 0, v1_x, v1_y, angles='xy', scale_units='xy', scale=1, color='blue',
        label=f'$\\vec{{v}}_1 = ({v1_x:.2f}\\hat{{i}} {v1_y:.2f}\\hat{{j}})$ m/s  (em t₁)')

#Desenha o vetor v2 (vermelho) partindo da origem (0,0)
ax.quiver(0, 0, v2_x, v2_y, angles='xy', scale_units='xy', scale=1, color='red',
        label=f'$\\vec{{v}}_2 = ({v2_x:.2f}\\hat{{i}} + {v2_y:.2f}\\hat{{j}})$ m/s  (em t₂)')

#--- Estilização e Formatação do Gráfico ---
#Define os limites dos eixos para que os vetores fiquem bem visíveis
limite_x = max(abs(v1_x), abs(v2_x)) + 2
limite_y = max(abs(v1_y), abs(v2_y)) + 2
ax.set_xlim(-limite_x, limite_x)
ax.set_ylim(-limite_y, limite_y)

#Adiciona as linhas dos eixos x e y que cruzam em (0, 0)
ax.axhline(0, color='black', linewidth=0.7)
ax.axvline(0, color='black', linewidth=0.7)

#Adiciona uma grade para facilitar a leitura
ax.grid(True, linestyle='--', alpha=0.6)

#Garante que a escala dos eixos seja a mesma
ax.set_aspect('equal', adjustable='box')

#Adiciona títulos, legendas e rótulos aos eixos
ax.set_title('Comparação dos Vetores Velocidade $\\vec{v}_1$ e $\\vec{v}_2$', fontsize=16)
ax.set_xlabel('Componente x da Velocidade ($v_x$) [m/s]', fontsize=12)
ax.set_ylabel('Componente y da Velocidade ($v_y$) [m/s]', fontsize=12)
ax.legend(fontsize=12, loc='upper left')

#Mostra o gráfico final
plt.show()