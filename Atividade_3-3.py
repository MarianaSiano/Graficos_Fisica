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