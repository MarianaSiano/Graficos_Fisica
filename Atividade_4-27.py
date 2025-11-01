import matplotlib.pyplot as plt

def corpo_livre_A(ax):
    # Caixa A
    ax.add_patch(plt.Rectangle((-0.6, 0), 1.2, 1.2, fc='#cccccc', ec='black', lw=2))
    ax.text(0, 0.6, 'A', fontsize=13, ha='center', va='center')

    # Força F para direita
    ax.arrow(-0.1, 1.2, 0.6, 0, head_width=0.12, head_length=0.2, fc='blue', ec='blue', lw=3)
    ax.text(0.3, 1.35, r'$\vec{F}$', color='blue', fontsize=15, ha='center')

    # Força de B em A para a esquerda (ação)
    ax.arrow(0.5, 0.6, -0.6, 0, head_width=0.12, head_length=0.2, fc='red', ec='red', lw=3)
    ax.text(-0.35, 0.7, r'$\vec{F}_{BA}$', color='red', fontsize=15, ha='left')

    # Normal para cima
    ax.arrow(0.6, 0.1, 0, 0.6, head_width=0.13, head_length=0.2, fc='green', ec='green', lw=3)
    ax.text(0.7, 0.4, r'$N_A$', color='green', fontsize=14)

    # Peso para baixo
    ax.arrow(-0.6, 1.1, 0, -0.6, head_width=0.13, head_length=0.18, fc='orange', ec='orange', lw=3)
    ax.text(-0.75, 0.8, r'$m_A g$', color='orange', fontsize=14)
    ax.set_xlim(-1, 1.2)
    ax.set_ylim(-0.2, 1.6)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Engradado A', fontsize=15)

def corpo_livre_B(ax):
    # Caixa B
    ax.add_patch(plt.Rectangle((-0.6, 0), 1.2, 1.2, fc='#cccccc', ec='black', lw=2))
    ax.text(0, 0.6, 'B', fontsize=13, ha='center', va='center')

    # Força de A em B para direita (reação)
    ax.arrow(-0.6, 0.6, 0.6, 0, head_width=0.12, head_length=0.2, fc='red', ec='red', lw=3)
    ax.text(0.2, 0.75, r'$\vec{F}_{AB}$', color='red', fontsize=15, ha='left')

    # Normal para cima
    ax.arrow(0.6, 0.1, 0, 0.6, head_width=0.13, head_length=0.2, fc='green', ec='green', lw=3)
    ax.text(0.7, 0.4, r'$N_B$', color='green', fontsize=14)

    # Peso para baixo
    ax.arrow(-0.6, 1.1, 0, -0.6, head_width=0.13, head_length=0.18, fc='orange', ec='orange', lw=3)
    ax.text(-0.75, 0.8, r'$m_B g$', color='orange', fontsize=14)
    ax.set_xlim(-1, 1.2)
    ax.set_ylim(-0.2, 1.6)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Engradado B', fontsize=15)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

corpo_livre_A(axs[0])
corpo_livre_B(axs[1])

plt.tight_layout()
plt.show()