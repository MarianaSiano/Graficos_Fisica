import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Valores aproximados para as forças (ajuste F_normal conforme cálculo)
peso = 75 * 9.8 # Peso em N
F_normal = -3067.5

fig, ax = plt.subplots(figsize=(4, 7))

# Retângulo que representa o corpo do homem
body = patches.Rectangle((0.4, 1.5), 0.2, 2, edgecolor='black', facecolor='lightgray')
ax.add_patch(body)

# Força normal (F_normal) para cima
ax.arrow(0.5, 3.5, 0, 1.5, head_width=0.09, head_length=0.2, fc='red', ec='red', length_includes_head=True)
ax.text(0.57, 4.8, f'Força Normal (N = {F_normal} N)', color='red', fontsize=11)

# Força peso (mg) para baixo
ax.arrow(0.5, 1.5, 0, -1.2, head_width=0.08, head_length=0.18, fc='blue', ec='blue', length_includes_head=True)
ax.text(0.55, 0.9, f'Peso (mg = {peso:.0f} N)', color='blue', fontsize=11)

# Ajustes finais
ax.set_xlim(0, 1)
ax.set_ylim(0, 5.5)
ax.axis('off')
ax.set_title('Diagrama de Corpo Livre\nHomem parando após queda', fontsize=13)
plt.tight_layout()

plt.show()