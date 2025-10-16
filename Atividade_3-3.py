import numpy as np

def calcular_vetor_posicao(t):
    """
    A equação do vetor é:
    r(t) = [4.0 + (2.5 * t^2)]î + (5.0 * t)ĵ

    Args:
    t (float): O tempo em segundos (s).

    Returns:
    numpy.ndarray: Um array NumPy representando o vetor posição [x, y] em centímetros (cm).
    """

    #Componente x do vetor
    x = 4.0 + (2.5 * (t ** 2))

    #Componente y do vetor
    y = 5.0 * t

    #Retorna o vetor como um array NumPy [x, y]
    return np.array([x, y])

def calcular_velocidade_media(t1, t2):
    """
    Calcula o vetor velocidade média entre dois instantes de tempo, t1 e t2.

    A fórmula é: v_med = (r(t2) - r(t1)) / (t2 - t1)

    Args:
        t1 (float): O tempo inicial em segundos (s).
        t2 (float): O tempo final em segundos (s).

    Returns:
        numpy.ndarray: Um array NumPy representando o vetor velocidade média [vx, vy] em cm/s.
    """

# Atividade
#Definir o tempo para o qual queremos calcular
t1 = 0.0 #em segundos
t2 = 2.0 #em segundos

#Chamar a função para obter o vetor posição
p1 = calcular_vetor_posicao(t1)
p2 = calcular_vetor_posicao(t2)