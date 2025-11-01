import matplotlib.pyplot as plt

def draw_free_body_diagram(ax, title):
    #Desenha a bola
    ball = plt.Circle((0, 0), 0.2, color='orange', ec='k', lw=2)
    ax.add_patch(ball)

    # Desenha a força peso
    ax.arrow(0, 0, 0, -0.8, head_width=0.08, head_length=0.15, fc='red', ec='red', lw=2)
    ax.text(0.1, -0.4, 'mg', color='red', fontsize=12, va='center', ha='left')

    # Configurações do gráfico
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-1.0, 0.5)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)

fig, axs = plt.subplots(1, 3, figsize=(10, 4))

titles = [
    '(a) Subida',
    '(b) Ponto mais alto',
    '(c) Descendo'
]

for ax, title in zip(axs, titles):
    draw_free_body_diagram(ax, title)

plt.tight_layout()
plt.show()