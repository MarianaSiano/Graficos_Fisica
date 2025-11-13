import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_vector(ax, origin, vector, color, label, arrowstyle='-|>', linewidth=2, alpha=1.0):
    ax.quiver(
        origin[0], origin[1], origin[2],
        vector[0], vector[1], vector[2],
        color=color, arrow_length_ratio=0.18, linewidth=linewidth, alpha=alpha
    )
    ax.text(
        origin[0] + vector[0]*1.08, origin[1] + vector[1]*1.08, origin[2] + vector[2]*1.08,
        label, fontsize=14, color=color, zorder=10
    )

# Posições (ajustes para se aproximar do seu quadro)
O = np.array([0, 0, 0])
r_i = np.array([2, 2, 2])
r_i1 = np.array([2.5, 1, 1.5])
r_b = np.array([3, 2.5, 2])

# Forças (exemplo ilustrativo)
F_i = np.array([1, 0.5, 1])
F_i1 = np.array([0.5, 0.7, 1.2])
F_b = np.array([1, 0.8, 0.4])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Vetores de posição
draw_vector(ax, O, r_i, 'royalblue', r'$\vec{r}_i$')
draw_vector(ax, O, r_i1, 'darkgreen', r'$\vec{r}_{i-1}$')
draw_vector(ax, O, r_b, 'purple', r'$\vec{r}_b$')

# Forças nos pontos
draw_vector(ax, r_i, F_i, 'blue', r'$\vec{F}_i$', linewidth=3, alpha=0.7)
draw_vector(ax, r_i1, F_i1, 'green', r'$\vec{F}_{i-1}$', linewidth=3, alpha=0.7)
draw_vector(ax, r_b, F_b, 'violet', r'$\vec{F}_b$', linewidth=3, alpha=0.7)

# Pontos principais
ax.scatter(*r_i, color='royalblue', s=50)
ax.scatter(*r_i1, color='darkgreen', s=50)
ax.scatter(*r_b, color='purple', s=50)
ax.text(*O, r'$O$', fontsize=16, color='black', zorder=10)

# Eixos
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])
ax.view_init(elev=25, azim=38)
plt.tight_layout()
plt.show()