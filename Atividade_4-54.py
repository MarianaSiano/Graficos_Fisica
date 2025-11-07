import matplotlib.pyplot as plt

def diagrama_bloco_6kg():
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.add_patch(plt.Rectangle((-0.5, -0.5), 1, 1, facecolor="#b0c4de", edgecolor="black", lw=2))
    ax.text(0, 0, "6 kg", fontsize=26, weight='bold', ha='center', va='center', color="black")

    # Peso para baixo
    ax.arrow(0, -0.5, 0, -1.2, head_width=0.18, head_length=0.22, fc="#ff8800", ec="#ff8800", lw=3, length_includes_head=True)
    ax.text(0, -2.0, r"$6kg\times9.8\ m/s^2$", fontsize=17, color="#ff8800", ha='center', va='center')

    # Tensão da corda para cima
    ax.arrow(0, 0.5, 0, 1.2, head_width=0.18, head_length=0.22, fc="blue", ec="blue", lw=3, length_includes_head=True)
    ax.text(-1.2, 2.0, r"Tensão da corda\npara cima", fontsize=15, color="#ff8800", ha='center', va='center')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.2, 2.2)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('./diagramas/dcl_bloco_6kg.png', bbox_inches='tight')
    plt.close(fig)

def diagrama_bloco_5kg():
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.add_patch(plt.Rectangle((-0.7, -0.5), 1.4, 1, facecolor="#b0c4de", edgecolor="black", lw=2))
    ax.text(0, 0, "5 kg", fontsize=26, weight='bold', ha='center', va='center', color="black")

    # Peso
    ax.arrow(0, -0.5, 0, -1.2, head_width=0.18, head_length=0.22, fc="#ff8800", ec="#ff8800", lw=3, length_includes_head=True)
    ax.text(0, -2.0, r"$5kg\times9.8\ m/s^2$", fontsize=17, color="#ff8800", ha='center', va='center')

    # Tensão da corda para cima
    ax.arrow(0, 0.5, 0, 1.2, head_width=0.18, head_length=0.22, fc="blue", ec="blue", lw=3, length_includes_head=True)
    ax.text(-1.2, 2.0, r"Tensão da corda\npara cima", fontsize=15, color="#ff8800", ha='center', va='center')

    # Força aplicada F para cima
    ax.arrow(0.3, 0.5, 0, 1.3, head_width=0.18, head_length=0.22, fc="green", ec="green", lw=3, length_includes_head=True)
    ax.text(1.2, 2.0, r"Força aplicada\n$F=200N$", fontsize=15, color="black", ha='center', va='center')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.2, 2.2)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('./diagramas/dcl_bloco_5kg.png', bbox_inches='tight')
    plt.close(fig)

def diagrama_corda():
    fig, ax = plt.subplots(figsize=(6, 2.6))

    # Barra horizontal representando a corda
    ax.add_patch(plt.Rectangle((-1.5, -0.35), 3.0, 0.7, facecolor="#e0e0e0", edgecolor="black", lw=2))
    ax.text(0, 0, "Corda 4 kg", fontsize=22, weight='bold', ha='center', va='center', color="black")

    # Tensão no topo da corda (seta azul para cima, texto laranja)
    ax.arrow(-0.3, 0.35, 0, 1.0, head_width=0.15, head_length=0.18, fc="blue", ec="blue", lw=3, length_includes_head=True)
    ax.text(-0.8, 1.05, "Tensão no topo", fontsize=14, color="#ff8800", ha='center')

    # Tensão na base (verde para baixo, texto verde)
    ax.arrow(0.3, -0.35, 0, -1.0, head_width=0.15, head_length=0.18, fc="green", ec="green", lw=3, length_includes_head=True)
    ax.text(0.85, -1.05, "Tensão na base", fontsize=14, color="green", ha='center')

    # Peso da corda (laranja, centralizado para baixo)
    ax.arrow(0, 0, 0, -0.95, head_width=0.12, head_length=0.15, fc="#ff8800", ec="#ff8800", lw=3, length_includes_head=True)
    ax.text(0.5, -0.7, r"$4kg\times9.8\ m/s^2$", fontsize=13, color="#ff8800", ha='center')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.7, 1.7)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('./diagramas/dcl_corda_4kg.png', bbox_inches='tight')
    plt.close(fig)

# Gere os diagramas
diagrama_bloco_6kg()
diagrama_bloco_5kg()
diagrama_corda()