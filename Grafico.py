#Atividade 3.3

import matplotlib.pyplot as plt
import numpy as np

#--- 1. Definição das Equações ---
#Equações de posição em função do tempo (t)
def x(t):
    return 2.5 * t**2

def y(t):
    return 5.0 * t

#Equações de velocidade em função do tempo (t)
def vx(t):
    return 5.0 * t

def vy(t):
    return 5.0

#--- 2. Geração de Dados para a Trajetória ---
#Cria 100 pontos de tempo entre t=0 e t=2 para uma curva suave
t_array = np.linspace(0, 2, 100)
x_traj = x(t_array)
y_traj = y(t_array)

#--- 3. Cálculo dos Vetores nos Pontos de Interesse ---
# Ponto e vetor em t=0s
t0 = 0
pos_t0 = (x(t0), y(t0))
vel_t0 = (vx(t0), vy(t0))

#Ponto e vetor em t=2s
t2 = 2
pos_t2 = (x(t2), y(t2))
vel_t2 = (vx(t2), vy(t2))

#--- 4. Criação do Gráfico (Plot) ---
#Cria a figura e os eixos para o gráfico
fig, ax = plt.subplots(figsize=(10, 8))

#Plota a trajetória
ax.plot(x_traj, y_traj, label='Trajetória do Ponto', color='blue', linewidth=2)

#Plota os pontos inicial e final
ax.scatter([pos_t0[0], pos_t2[0]], [pos_t0[1], pos_t2[1]], color='black', zorder=5)
ax.text(pos_t0[0] - 1.5, pos_t0[1], 't=0s', fontsize=12)
ax.text(pos_t2[0] + 0.5, pos_t2[1], 't=2s', fontsize=12)


#Plota os vetores velocidade usando ax.quiver()
#Formato: quiver(x_start, y_start, x_component, y_component, ...)
ax.quiver(pos_t0[0], pos_t0[1], vel_t0[0], vel_t0[1], 
        angles='xy', scale_units='xy', scale=1, color='red', label='Vetor Velocidade (t=0s)')

ax.quiver(pos_t2[0], pos_t2[1], vel_t2[0], vel_t2[1], 
        angles='xy', scale_units='xy', scale=1, color='green', label='Vetor Velocidade (t=2s)')

#--- 5. Configuração e Estilo do Gráfico ---
#Títulos e rótulos dos eixos
ax.set_title('Trajetória e Vetores Velocidade', fontsize=16)
ax.set_xlabel('Posição x (cm)', fontsize=12)
ax.set_ylabel('Posição y (cm)', fontsize=12)

#Garante que a escala dos eixos seja a mesma para não distorcer os ângulos
ax.set_aspect('equal', adjustable='box')

#Adiciona uma grade para facilitar a leitura
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

#Define os limites dos eixos para uma boa visualização
ax.set_xlim(-2, 22)
ax.set_ylim(-2, 17)

#Adiciona a legenda
ax.legend(fontsize=12)

#--- 6. Exibir e Salvar o Gráfico ---
#Salva a imagem em um arquivo PNG
plt.savefig('grafico_trajetoria.png', dpi=300, bbox_inches='tight')

#Mostra o gráfico em uma janela
plt.show()

print("Gráfico gerado e salvo como 'grafico_trajetoria.png'")