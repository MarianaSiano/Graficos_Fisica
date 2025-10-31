import matplotlib.pyplot as plt
import numpy as np

def plot_vectors_corrigido(case):
    F = 1
    plt.figure(figsize=(5,5))
    plt.axis('equal')
    plt.grid(True)
    plt.xlim(-2,2)
    plt.ylim(-2,2)

    if case == 'a':
        offset = 0.05
        A = np.array([F, 0])
        B = np.array([F, 0])
        R = A + B
        plt.quiver(0, offset, A[0], A[1], color='r', angles='xy', scale_units='xy', scale=1, label='A')
        plt.quiver(0, -offset, B[0], B[1], color='b', angles='xy', scale_units='xy', scale=1, label='B')
        plt.quiver(0, 0, R[0], R[1], color='g', angles='xy', scale_units='xy', scale=1, label='R')
        plt.title('a) Ângulo 0° (módulo 2F)')
    elif case == 'b':
        A = np.array([F, 0])
        B = np.array([0, F])
        R = A + B
        plt.quiver(0, 0, A[0], A[1], color='r', angles='xy', scale_units='xy', scale=1, label='A')
        plt.quiver(0, 0, B[0], B[1], color='b', angles='xy', scale_units='xy', scale=1, label='B')
        plt.quiver(0, 0, R[0], R[1], color='g', angles='xy', scale_units='xy', scale=1, label='R')
        plt.title('b) Ângulo 90° (módulo raiz(2)F)')
    elif case == 'c': 
        A = np.array([F, 0])
        B = np.array([-F, 0])
        plt.quiver(0, 0.05, A[0], A[1], color='r', angles='xy', scale_units='xy', scale=1, label='A')
        plt.quiver(0, -0.05, B[0], B[1], color='b', angles='xy', scale_units='xy', scale=1, label='B')
        plt.scatter([0], [0], color='g', s=60, label='R (nula)')
        plt.title('c) Ângulo 180° (módulo zero)')
    plt.legend(loc='upper right')
    plt.show()

# Gera os três desenhos corrigidos
for caso in ['a', 'b', 'c']:
    plot_vectors_corrigido(caso)