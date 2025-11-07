import matplotlib.pyplot as plt

def draw_dcl_bloco_6kg():
    fig, ax = plt.subplots(figsize=(5, 6))
    # Quadrado representando o bloco
    ax.add_patch(plt.Rectangle((-0.5, -0.5), 1, 1, facecolor="#b0c4de", edgecolor="black", lw=2))
    ax.text(0, 0, "6 kg", fontsize=26, weight='bold', ha='center', va='center', color="black")
    
    # Peso para baixo (seta e texto laranja)
    ax.arrow(0, -0.5, 0, -1.2, head_width=0.18, head_length=0.22, fc="#ff8800", ec="#ff8800", lw=3, length_includes_head=True)
    ax.text(0, -2.0, r"$6kg\times9.8 m/s^2$", fontsize=17, color="#ff8800", ha='center', va='center')
    
    # Tensão da corda para cima (seta azul, texto laranja)
    ax.arrow(0, 0.5, 0, 1.2, head_width=0.18, head_length=0.22, fc="blue", ec="blue", lw=3, length_includes_head=True)
    ax.text(-1.2, 2.0, r"Tensão dacorda para cima", fontsize=17, color="#ff8800", ha='center', va='center') # cor de texto igual ao peso
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.2, 2.2)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('./diagramas/dcl_bloco_6kg.png', bbox_inches='tight')
    plt.close(fig)

def draw_dcl_bloco_5kg():
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.add_patch(plt.Rectangle((-0.7, -0.5), 1.4, 1, facecolor="#b0c4de", edgecolor="black", lw=2))
    ax.text(0, 0, "5 kg", fontsize=26, weight='bold', ha='center', va='center', color="black")
    
    # Peso para baixo (seta/legenda laranja)
    ax.arrow(0, -0.5, 0, -1.2, head_width=0.18, head_length=0.22, fc="#ff8800", ec="#ff8800", lw=3, length_includes_head=True)
    ax.text(0, -2.0, r"$5kg\times9.8 m/s^2$", fontsize=17, color="#ff8800", ha='center', va='center')
    
    # Tensão da corda para cima (seta azul, texto laranja)
    ax.arrow(0, 0.5, 0, 1.2, head_width=0.18, head_length=0.22, fc="blue", ec="blue", lw=3, length_includes_head=True)
    ax.text(-1.2, 2.0, r"Tensão da corda para cima", fontsize=13, color="#ff8800", ha='center', va='center')
    
    # Força aplicada F para cima (seta/texto verde)
    ax.arrow(0.3, 0.5, 0, 1.3, head_width=0.18, head_length=0.22, fc="green", ec="green", lw=3, length_includes_head=True)
    ax.text(1.2, 2.0, r"Força aplicada $F=200N$", fontsize=13, color="black", ha='center', va='center')
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.2, 2.2)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('./diagramas/dcl_bloco_5kg.png', bbox_inches='tight')
    plt.close(fig)

# Gere os diagramas
draw_dcl_bloco_6kg()
draw_dcl_bloco_5kg()