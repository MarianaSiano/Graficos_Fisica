import matplotlib.pyplot as plt

def desenha_caixa(ax, x, y, label, color):
    ax.add_patch(plt.Rectangle((x-0.5, y-0.5), 1.0, 1.0, ec='black', fc=color, lw=2))
    ax.text(x, y, label, fontsize=24, ha='center', va='center', fontweight='bold', color='black')

def desenha_vetor(ax, x, y, dx, dy, cor, label, pos_label, size=3):
    ax.arrow(x, y, dx, dy, head_width=0.12, head_length=0.19, fc=cor, ec=cor, lw=size, length_includes_head=True)
    ax.text(pos_label[0], pos_label[1], label, color=cor, fontsize=18, va='center', ha='center', fontweight='bold')

fig, ax = plt.subplots(figsize=(12, 6))

# Engradado A
desenha_caixa(ax, -2, 0, 'A', '#ffe08a')
desenha_vetor(ax, -2, 0.4, 0, 1.2, 'green', r'$N_A$', [-2, 1.75], 3)
desenha_vetor(ax, -2, -0.4, 0, -1.2, 'orange', r'$m_Ag$', [-2, -1.8], 3)
desenha_vetor(ax, -1.5, 0, 1.2, 0, 'blue', r'$\vec{F}$', [-0.3, 0.1], 3)
desenha_vetor(ax, -2.5, 0, -1.2, 0, 'red', r'$\vec{F}_{BA}$', [-3.7, 0.12], 3)

# Engradado B
desenha_caixa(ax, 2, 0, 'B', '#7eccec')
desenha_vetor(ax, 2, 0.4, 0, 1.2, 'green', r'$N_B$', [2, 1.75], 3)
desenha_vetor(ax, 2, -0.4, 0, -1.2, 'orange', r'$m_Bg$', [2, -1.8], 3)
desenha_vetor(ax, 1.5, 0, -1.2, 0, 'red', r'$\vec{F}_{AB}$', [0.3, -0.12], 3)

# Configurações
ax.text(-2, 2.1, "Engradado A", fontsize=20, ha='center')
ax.text(2, 2.1, "Engradado B", fontsize=20, ha='center')
ax.set_xlim(-5, 5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()