import matplotlib.pyplot as plt
import numpy as np

def diagrama(m, alpha_graus, caso, mu = 0):
    g = 9.8 # Aceleração da gravidade (m/s^2)
    alpha = np.radians(alpha_graus)

    # Componentes das forças
    peso = m * g
    normal = peso * np.cos(alpha)
    fg = peso * np.sin(alpha)

    if caso == 'a':
        # Descendo, sem atrito
        forces = {'Peso (mg)': [0, -1], 'Normal (N)': [np.sin(alpha), np.cos(alpha)]}
    elif caso == 'b':
        # Subindo, sem atrito (forças iguais ao a)
        forces = {'Peso (mg)': [0, -1], 'Normal (N)': [np.sin(alpha), np.cos(alpha)]}
    elif caso == 'c':
        # subindo, com atrito
        atrito = mu * normal
        forces = {
            'Peso (mg)': [0, -1],
            'Normal (N)': [np.sin(alpha), np.cos(alpha)],
            'Atrito (f)': [-np.cos(alpha), np.sin(alpha)]
        }
    else:
        raise ValueError('caso deve ser "a", "b" ou "c"')

    plt.figure(figsize=(6, 6))
    plt.title(f"Diagrama de Corpo Livre ({caso})")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid(True)
    plt.plot(0, 0, 'ks', markersize=15)  # o bloco

    for nome, vetor in forces.items():
        plt.arrow(0, 0, vetor[0], vetor[1], head_width=0.1, head_length=0.15)
        plt.text(vetor[0]*1.1, vetor[1]*1.1, nome, fontsize=12)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f'./diagramas/figuure_5-27-{caso}.png')

m = 2.0           # Massa do bloco (kg)
alpha_graus = 30  # Ângulo do plano inclinado (graus)
mu = 0.25         # Coeficiente de atrito cinético (apenas para o caso c)

diagrama(m, alpha_graus, 'a')
diagrama(m, alpha_graus, 'b')
diagrama(m, alpha_graus, 'c', mu)