import matplotlib.pyplot as plt
import numpy as np

# Ângulo e forças
theta = 37  # graus abaixo da horizontal
F = 40      # N
m = 12      # kg

def draw_chair_diagram(ax):
    # Desenha a cadeira
    ax.add_patch(plt.Rectangle((-0.5, -0.2), 1.0, 0.4, ec='black', fc='#ffe08a', lw=2))
    ax.text(0, 0, "cadeira", fontsize=15, ha='center', va='center', fontweight='bold', color='black')

    # Peso (mg)
    ax.arrow(0, -0.2, 0, -1.1, head_width=0.09, head_length=0.13, fc='orange', ec='orange', lw=3, length_includes_head=True)
    ax.text(0.1, -1.2, r'$mg$', color='orange', fontsize=14, va='center', ha='left')

    # Normal (N)
    ax.arrow(0, 0.2, 0, 1.0, head_width=0.09, head_length=0.13, fc='green', ec='green', lw=3, length_includes_head=True)
    ax.text(0.07, 1.22, r'$N$', color='green', fontsize=14, va='center', ha='left')

    # Atrito
    ax.arrow(-0.5, -0.05, -0.7, 0, head_width=0.09, head_length=0.15, fc='red', ec='red', lw=3, length_includes_head=True)
    ax.text(-1.25, -0.05, r'$\vec{f}_{atrito}$', color='red', fontsize=14, va='center', ha='right')

    # Força F inclinada (37° abaixo horizontal)
    ang_rad = np.deg2rad(-theta)
    dx = np.cos(ang_rad)
    dy = np.sin(ang_rad)
    ax.arrow(0.5, 0, 1.2*dx, 1.2*dy, head_width=0.09, head_length=0.15, fc='blue', ec='blue', lw=3, length_includes_head=True)
    ax.text(0.5+1.4*dx, 0+1.2*dy, r'$\vec{F}$', color='blue', fontsize=14, va='center', ha='left')

    # Configurações visuais
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('Diagrama de corpo livre da cadeira', fontsize=15)

fig, ax = plt.subplots(figsize=(7, 7))
draw_chair_diagram(ax)
plt.tight_layout()
plt.show()