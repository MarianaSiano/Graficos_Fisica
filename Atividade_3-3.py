import numpy as np
import math
import matplotlib.pyplot as plt

#--- DEFINIÇÃO DAS FUNÇÕES DE CÁLCULO ---

def calcular_vetor_posicao(t: float) -> np.ndarray:
    """
    Calcula o vetor posição r(t) para um dado tempo t.
    Equação: r(t) = [4.0 + (2.5 * t^2)]î + (5.0 * t)ĵ
    """
    x = 4.0 + (2.5 * (t ** 2))
    y = 5.0 * t
    return np.array([x, y])

def calcular_velocidade_media(t1: float, t2: float) -> np.ndarray:
    """
    Calcula o vetor velocidade média entre dois instantes de tempo.
    Fórmula: v_med = (r(t2) - r(t1)) / (t2 - t1)
    """
    delta_t = t2 - t1
    if delta_t == 0:
        raise ValueError("O tempo inicial (t1) e final (t2) não podem ser iguais.")
    r1 = calcular_vetor_posicao(t1)
    r2 = calcular_vetor_posicao(t2)
    delta_r = r2 - r1
    return delta_r / delta_t