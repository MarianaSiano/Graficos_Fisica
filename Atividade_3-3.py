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

def calcular_velocidade_instantanea(t: float) -> np.ndarray:
    """
    Calcula o vetor velocidade instantânea v(t) para um dado tempo t.
    Equação: v(t) = (5.0 * t)î + 5.0ĵ
    """
    vx = 5.0 * t
    vy = 5.0
    return np.array([vx, vy])

def analisar_vetor(vetor: np.ndarray) -> tuple[float, float]:
    """
    Calcula o módulo e a direção (ângulo em graus) de um vetor.
    """
    modulo = np.linalg.norm(vetor)
    if modulo == 0:
        #Retorna uma string para o ângulo, pois é indefinido
        return modulo, "Indefinida"
    angulo_rad = math.atan2(vetor[1], vetor[0])
    angulo_graus = math.degrees(angulo_rad)
    return modulo, angulo_graus