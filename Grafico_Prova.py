import matplotlib.pyplot as plt

# Vetor aceleração: (0i, 2j)
origin = [0, 0] # Origem do vetor
components = [0, 2] # Componentes do vetor

plt.figure(figsize=(5,5))
plt.quiver(*origin, *components, angles='xy', scale_units='xy', scale=1, color='blue')
plt.xlim(-1, 1)
plt.ylim(0, 3)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Vetor aceleração a = 0i + 2j')
plt.grid(True)
plt.text(0, 2.2, 'a = 2j', color='blue')
plt.savefig(f'./graficos/questao_1-prova.png')