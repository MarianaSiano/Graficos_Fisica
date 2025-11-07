import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Parâmetros físicos
m_elo = 0.3
g = 9.8
num_elos = 3
F_fio = 12.0

peso_elo = m_elo * g
peso_total = num_elos * peso_elo
m_total = m_elo * num_elos
acel = (F_fio - peso_total) / m_total

t_sup = F_fio
mass2 = 2 * m_elo
t_med = mass2 * g + mass2 * acel
t_inf = m_elo * g + m_elo * acel

def dcf_plot(ax, title, label, T_cima, P, left_arrow=None, right_arrow=None, color_quad='#FFD580'):
    # Quadrado (1x1) centralizado em (0,0)
    sq = Rectangle((-0.5, -0.5), 1, 1, linewidth=2, edgecolor='black', facecolor=color_quad)
    ax.add_patch(sq)
    # Nome centralizado
    ax.text(0, 0, label, fontsize=17, weight='bold', ha='center', va='center', color='black')
    # Peso (seta laranja para baixo) - começa na base
    ax.arrow(0, -0.5, 0, -0.7, head_width=0.15, head_length=0.17, fc='#FFA500', ec='#FFA500', linewidth=3, length_includes_head=True)
    ax.text(0.23, -1.05, '$mg$', color='#FFA500', fontsize=13, ha='left', va='center')
    # Tensão cima (seta verde para cima) - começa no topo
    if T_cima:
        ax.arrow(0, 0.5, 0, 0.7, head_width=0.15, head_length=0.17, fc='green', ec='green', linewidth=3, length_includes_head=True)
        ax.text(0.23, 1.05, '$T$', color='green', fontsize=13, ha='left', va='center')
    # Setas horizontais (começam nas laterais)
    if left_arrow:
        ax.arrow(-0.5, 0, -0.7, 0, head_width=0.15, head_length=0.15, fc=left_arrow['color'], ec=left_arrow['color'], linewidth=3, length_includes_head=True)
        ax.text(-1.28, 0.11, left_arrow['label'], color=left_arrow['color'], fontsize=13, ha='right', va='center')
    if right_arrow:
        ax.arrow(0.5, 0, 0.7, 0, head_width=0.15, head_length=0.15, fc=right_arrow['color'], ec=right_arrow['color'], linewidth=3, length_includes_head=True)
        ax.text(1.29, 0.11, right_arrow['label'], color=right_arrow['color'], fontsize=13, ha='left', va='center')
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.3,1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title)

fig, axes = plt.subplots(1, 4, figsize=(18,5))

# Corrente como um todo
dcf_plot(axes[0],'Corrente Inteira','Corrente', F_fio, peso_total, color_quad='#CCFFCC')
# Elo superior
dcf_plot(axes[1],'Elo Superior','Elo 1', t_sup, peso_elo, right_arrow={'label':"$F_{12}$", 'color':'#0066FF'}, color_quad='#FFD580')
# Elo do meio
dcf_plot(axes[2],'Elo Meio','Elo 2', t_med, peso_elo, left_arrow={'label':"$F_{21}$",'color':'#FF6666'}, right_arrow={'label':"$F_{23}$",'color':'#0066FF'}, color_quad='#80BFFF')
# Elo inferior
dcf_plot(axes[3],'Elo Inferior','Elo 3', t_inf, peso_elo, left_arrow={'label':"$F_{32}$",'color':'#FF6666'}, color_quad='#B0E57C')

plt.suptitle('Diagramas de Corpo Livre', fontsize=17)
plt.tight_layout(rect=[0,0,1,0.93])
plt.savefig('./diagramas/figure_4-57.png')