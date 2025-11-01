import matplotlib.pyplot as plt

def corpo_livre_bola_mao(ax, titulo):
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
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(titulo, fontsize=14)

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
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(titulo, fontsize=14)

fig, axs = plt.subplots(1, 4, figsize=(16, 6))

titulos = [
    'Bola na mão',
    '(a) Subida após lançamento',
    '(b) Ponto mais alto',
    '(c) Descendo'
]

corpo_livre_bola_mao(axs[0], titulos[0])
corpo_livre_bola_livre(axs[1], titulos[1])
corpo_livre_bola_livre(axs[2], titulos[2])
corpo_livre_bola_livre(axs[3], titulos[3])

plt.tight_layout()
plt.show()