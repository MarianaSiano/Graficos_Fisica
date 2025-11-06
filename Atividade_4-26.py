import matplotlib.pyplot as plt
import numpy as np

def corpo_livre_bola_mao(ax, titulo):
    # Vertical: força normal para cima
    rect = plt.Rectangle((-1, -2), 2, 4, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    bola = plt.Circle((0, 1), 0.7, color='orange', ec='k', lw=2)
    ax.add_patch(bola)
    ax.arrow(0, 1, 0, -1.5, head_width=0.15, head_length=0.25, fc='red', ec='red', lw=3, length_includes_head=True)
    ax.text(0.18, 0.25, 'mg', color='red', fontsize=13, va='center', ha='left')
    ax.arrow(0, 1, 0, 1.2, head_width=0.15, head_length=0.25, fc='blue', ec='blue', lw=3, length_includes_head=True)
    ax.text(0.18, 2.0, 'N', color='blue', fontsize=13, va='center', ha='left')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(titulo, fontsize=13)

def corpo_livre_bola_mao_inclinado(ax, titulo, angulo):
    # Inclinado: força normal a 60 graus
    rect = plt.Rectangle((-1, -2), 2, 4, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    bola = plt.Circle((0, 1), 0.7, color='orange', ec='k', lw=2)
    ax.add_patch(bola)
    ax.arrow(0, 1, 0, -1.5, head_width=0.15, head_length=0.25, fc='red', ec='red', lw=3, length_includes_head=True)
    ax.text(0.18, 0.25, 'mg', color='red', fontsize=13, va='center', ha='left')
    dx = 1.2 * np.cos(np.deg2rad(60))
    dy = 1.2 * np.sin(np.deg2rad(60))
    ax.arrow(0, 1, dx, dy, head_width=0.15, head_length=0.25, fc='blue', ec='blue', lw=3, length_includes_head=True)
    ax.text(dx+0.02, dy+1.0, 'N', color='blue', fontsize=13, va='center', ha='left')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(titulo, fontsize=13)

def corpo_livre_bola_livre(ax, titulo):
    rect = plt.Rectangle((-1, -2), 2, 4, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    bola = plt.Circle((0, 1), 0.7, color='orange', ec='k', lw=2)
    ax.add_patch(bola)
    ax.arrow(0, 1, 0, -1.5, head_width=0.15, head_length=0.25, fc='red', ec='red', lw=3, length_includes_head=True)
    ax.text(0.18, 0.25, 'mg', color='red', fontsize=13, va='center', ha='left')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(titulo, fontsize=13)

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# Primeira linha: vertical (a, b, c)
titulos1 = [
    'Bola na mão (vertical)', '(a) Subida', '(b) Ponto mais alto', '(c) Descendo'
]
corpo_livre_bola_mao(axs[0,0], titulos1[0])
corpo_livre_bola_livre(axs[0,1], titulos1[1])
corpo_livre_bola_livre(axs[0,2], titulos1[2])
corpo_livre_bola_livre(axs[0,3], titulos1[3])

# Segunda linha: inclinado (letra d)
titulos2 = [
    'Bola na mão (inclinado)', '(d) Subida (60°)', '(d) Ponto mais alto (60°)', '(d) Descendo (60°)'
]
corpo_livre_bola_mao_inclinado(axs[1,0], titulos2[0], 60)
corpo_livre_bola_livre(axs[1,1], titulos2[1])
corpo_livre_bola_livre(axs[1,2], titulos2[2])
corpo_livre_bola_livre(axs[1,3], titulos2[3])

plt.tight_layout()
plt.savefig('./diagramas/figure_4-26.png')