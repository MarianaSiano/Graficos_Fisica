import matplotlib.pyplot as plt
import numpy as np

# Dados do problema
raio = 0.16
comprimento_fio = 0.30
angulo = np.arcsin(raio / comprimento_fio)
angulo_graus = np.degrees(angulo)

# Centro da bola
x0, y0 = 0, 0

# Calculando a direção das forças
# Peso: vertical para baixo
# Tensão: no ângulo do fio (theta)
# Normal: horizontal para a direita

plt.figure(figsize=(6,6))

# Bola
bola = plt.Circle((x0,y0), raio, fc='none', ec='black', lw=2)
plt.gca().add_patch(bola)

# Peso
plt.arrow(x0, y0, 0, -0.14, head_width=0.02, head_length=0.03, color='blue', length_includes_head=True)
plt.text(x0-0.02, y0-0.14, 'P', fontsize=14, color='blue')

# Tensão
plt.arrow(x0, y0, comprimento_fio*np.sin(angulo)*0.85, comprimento_fio*np.cos(angulo)*0.85,head_width=0.02, head_length=0.03, color='green', length_includes_head=True)
plt.text(x0+comprimento_fio*np.sin(angulo)*0.65, y0+comprimento_fio*np.cos(angulo)*0.70, 'T', fontsize=14, color='green')

# Força normal da parede
plt.arrow(x0, y0, -0.15, 0, head_width=0.02, head_length=0.03, color='red', length_includes_head=True)
plt.text(x0-0.16, y0+0.02, 'N', fontsize=14, color='red')

# Parede
plt.plot([-raio-0.05,-raio-0.05],[-0.25,0.25], 'k', lw=3)
plt.text(-raio-0.07, 0.18, 'Parede', rotation=90)

plt.xlim(-0.25,0.25)
plt.ylim(-0.25,0.25)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title('Diagrama de Corpo Livre da Bola')
plt.savefig('./diagramas/figure_5-13.png')