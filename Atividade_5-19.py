import matplotlib.pyplot as plt
import numpy as np

# Dados básicos
comprimento_seta = 2
lado = 0.8

fig, ax = plt.subplots(figsize=(8,5))

# Tijolos
centro_tijolos = np.array([0,0])
lower_left_tijolos = centro_tijolos + np.array([-lado/2, -lado/2])
tijolos_square = plt.Rectangle(lower_left_tijolos, lado, lado, color='saddlebrown')
plt.gca().add_patch(tijolos_square)

# Peso tijolos (sai do centro da base inferior)
origem_peso = centro_tijolos + np.array([0, -lado/2])
plt.arrow(*origem_peso, 0, -comprimento_seta, width=0.05, color="b", head_width=0.25, length_includes_head=True)
plt.text(* (origem_peso + np.array([-0.1, -comprimento_seta*1.1])), r'$P_1$', fontsize=14, color="b", ha="center")

# Tensão tijolos (sai do centro do topo)
origem_tensao = centro_tijolos + np.array([0, lado/2])
plt.arrow(*origem_tensao, 0, comprimento_seta, width=0.05, color="r", head_width=0.25, length_includes_head=True)
plt.text(* (origem_tensao + np.array([0, comprimento_seta*1.1])), r'$T$', fontsize=14, color="r", ha="center")
plt.text(-0.6, lado*2, "Tijolos\n$15\\,kg$", fontsize=12, ha="center", color="saddlebrown")

# Contrapeso
centro_contrapeso = np.array([4,0])
lower_left_contrapeso = centro_contrapeso + np.array([-lado/2, -lado/2])
contrapeso_square = plt.Rectangle(lower_left_contrapeso, lado, lado, color='gray')
plt.gca().add_patch(contrapeso_square)

# Peso contrapeso (sai do centro da base inferior)
origem_peso2 = centro_contrapeso + np.array([0, -lado/2])
plt.arrow(*origem_peso2, 0, -comprimento_seta, width=0.05, color="b", head_width=0.25, length_includes_head=True)
plt.text(* (origem_peso2 + np.array([0.13, -comprimento_seta*1.1])), r'$P_2$', fontsize=14, color="b", ha="center")

# Tensão contrapeso (sai do centro do topo)
origem_tensao2 = centro_contrapeso + np.array([0, lado/2])
plt.arrow(*origem_tensao2, 0, comprimento_seta, width=0.05, color="r", head_width=0.25, length_includes_head=True)
plt.text(* (origem_tensao2 + np.array([0, comprimento_seta*1.1])), r'$T$', fontsize=14, color="r", ha="center")
plt.text(4.8, lado*2, "Contrapeso\n$28\\,kg$", fontsize=12, ha="center", color="gray")

# Ajustes finais do gráfico
plt.xlim(-2, 6)
plt.ylim(-3, 3)
plt.axis('off')
plt.savefig('./diagramas/figure_5-19.png')