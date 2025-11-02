import matplotlib.pyplot as plt

def diagrama_caixa_4kg(ax):
    ax.add_patch(plt.Rectangle((-0.5, 0), 1.0, 1.0, ec='black', fc='#b0c4de', lw=2))
    ax.text(0, 0.7, '4 kg', fontsize=18, weight='bold', ha='center', va='center')

    # Peso
    ax.arrow(0, 0, 0, -1.0, head_width=0.12, head_length=0.17, fc='orange', ec='orange', lw=3, length_includes_head=True)
    ax.text(0.1, -0.9, r'$m_1 g$', color='orange', fontsize=15)

    # Normal
    ax.arrow(0, 1.0, 0, 0.8, head_width=0.12, head_length=0.17, fc='green', ec='green', lw=3, length_includes_head=True)
    ax.text(0.1, 1.8, r'$N_1$', color='green', fontsize=15)

    # Tensão para direita
    ax.arrow(0.5, 0.5, 1.0, 0, head_width=0.12, head_length=0.17, fc='blue', ec='blue', lw=3, length_includes_head=True)
    ax.text(1.6, 0.45, r'$T$', color='blue', fontsize=15)
    ax.set_xlim(-1.2, 2.5)
    ax.set_ylim(-1.2, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Caixa de 4 kg', fontsize=15)

def diagrama_caixa_6kg(ax):
    ax.add_patch(plt.Rectangle((-0.5, 0), 1.0, 1.0, ec='black', fc='#87ceeb', lw=2))
    ax.text(0, 0.7, '6 kg', fontsize=18, weight='bold', ha='center', va='center')

    # Peso
    ax.arrow(0, 0, 0, -1.0, head_width=0.12, head_length=0.17, fc='orange', ec='orange', lw=3, length_includes_head=True)
    ax.text(0.1, -0.9, r'$m_2 g$', color='orange', fontsize=15)

    # Normal
    ax.arrow(0, 1.0, 0, 0.8, head_width=0.12, head_length=0.17, fc='green', ec='green', lw=3, length_includes_head=True)
    ax.text(0.1, 1.8, r'$N_2$', color='green', fontsize=15)

    # Tensão para esquerda
    ax.arrow(-0.5, 0.5, -1.0, 0, head_width=0.12, head_length=0.17, fc='blue', ec='blue', lw=3, length_includes_head=True)
    ax.text(-1.6, 0.45, r'$T$', color='blue', fontsize=15, ha='right')

    # Força F para direita
    ax.arrow(0.5, 0.5, 1.2, 0, head_width=0.12, head_length=0.17, fc='red', ec='red', lw=3, length_includes_head=True)
    ax.text(1.7, 0.45, r'$F$', color='red', fontsize=15)
    ax.set_xlim(-2, 2.5)
    ax.set_ylim(-1.2, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Caixa de 6 kg', fontsize=15)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
diagrama_caixa_4kg(axs[0])
diagrama_caixa_6kg(axs[1])
plt.tight_layout()
plt.show()