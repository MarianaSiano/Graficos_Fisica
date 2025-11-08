import matplotlib.pyplot as plt
import numpy as np

# Ângulo da rampa
angulo = 35  # graus
angulo_rad = np.radians(angulo)

# Comprimento das setas das forças (valores arbitrários para visualização)
F_peso = 1.9
F_normal = 1.9
F_tensao = 1.9

# Centro da bola
bola_centro = np.array([0, 0])
raio = 0.5

# Peso: vertical para baixo
peso_vec = np.array([0, -F_peso])

# Normal: perpendicular à rampa (subindo e para a esquerda)
normal_direcao = np.array([-np.sin(angulo_rad), np.cos(angulo_rad)])
normal_vec = normal_direcao * F_normal

# Tensão: horizontal para a esquerda
tensao_vec = np.array([-F_tensao, 0])

fig, ax = plt.subplots(figsize=(7,6))

# Bola
bola = plt.Circle(bola_centro, raio, color='silver', ec='k', zorder=5)
ax.add_patch(bola)

# Forças
ax.arrow(*bola_centro, *peso_vec, color='b', width=0.03, head_width=0.12, length_includes_head=True)
ax.arrow(*bola_centro, *normal_vec, color='g', width=0.03, head_width=0.12, length_includes_head=True)
ax.arrow(*bola_centro, *tensao_vec, color='r', width=0.03, head_width=0.12, length_includes_head=True)

# Legenda das forças
ax.text(*(bola_centro + peso_vec*1.15), 'mg', color='b', fontsize=14)
ax.text(*(bola_centro + normal_vec*1.1), 'N', color='g', fontsize=14)
ax.text(*(bola_centro + tensao_vec*1.1), 'T', color='r', fontsize=14)

# Ajustes finais
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig('./diagramas/figure_5-15.png')