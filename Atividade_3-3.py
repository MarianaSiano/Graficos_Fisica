import numpy as np

# --- DEFINIÇÃO DAS FUNÇÕES DE CÁLCULO ---

def calcular_vetor_posicao(t: float) -> np.ndarray:
    """
    Calcula o vetor posição r(t) para um dado tempo t.

    A equação do vetor é: r(t) = [4.0 + (2.5 * t^2)]î + (5.0 * t)ĵ

    Args:
        t (float): O tempo em segundos (s).

    Returns:
        numpy.ndarray: Um array NumPy representando o vetor posição [x, y] em cm.
    """
    x = 4.0 + (2.5 * (t ** 2))
    y = 5.0 * t
    return np.array([x, y])

def calcular_velocidade_media(t1: float, t2: float) -> np.ndarray:
    """
    Calcula o vetor velocidade média entre dois instantes de tempo.

    A fórmula é: v_med = (r(t2) - r(t1)) / (t2 - t1)

    Args:
        t1 (float): O tempo inicial em segundos (s).
        t2 (float): O tempo final em segundos (s).

    Returns:
        numpy.ndarray: Vetor velocidade média [vx, vy] em cm/s.
    
    Raises:
        ValueError: Se t1 e t2 forem iguais, para evitar divisão por zero.
    """
    delta_t = t2 - t1
    if delta_t == 0:
        raise ValueError("O tempo inicial (t1) e final (t2) não podem ser iguais.")

    r1 = calcular_vetor_posicao(t1)
    r2 = calcular_vetor_posicao(t2)
    delta_r = r2 - r1
    
    velocidade_media = delta_r / delta_t
    return velocidade_media

def calcular_velocidade_instantanea(t: float) -> np.ndarray:
    """
    Calcula o vetor velocidade instantânea v(t) para um dado tempo t.

    A equação é a derivada do vetor posição: v(t) = (5.0 * t)î + 5.0ĵ

    Args:
        t (float): O instante de tempo em segundos (s).

    Returns:
        numpy.ndarray: Vetor velocidade instantânea [vx, vy] em cm/s.
    """
    vx = 5.0 * t
    vy = 5.0
    return np.array([vx, vy])

if __name__ == "__main__":
    #Definição dos instantes de tempo de interesse
    t_inicial = 0.0
    t_final = 2.0

    print(f"--- ANÁLISE CINEMÁTICA PARA O INTERVALO DE t={t_inicial}s a t={t_final}s ---")

    #--- Cálculos ---
    posicao_t0 = calcular_vetor_posicao(t_inicial)
    posicao_t2 = calcular_vetor_posicao(t_final)
    
    try:
        #Cálculo da velocidade média no intervalo [0, 2]
        v_media = calcular_velocidade_media(t_inicial, t_final)
    except ValueError as e:
        v_media = f"Erro: {e}"

    #Cálculo da velocidade instantânea em t=0 e t=2
    velocidade_t0 = calcular_velocidade_instantanea(t_inicial)
    velocidade_t2 = calcular_velocidade_instantanea(t_final)

    #--- Exibição dos resultados ---
    print("\n1. Posição:")
    print(f"   - Posição em t = {t_inicial}s: r({t_inicial}) = {posicao_t0[0]} î + {posicao_t0[1]} ĵ (em cm)")
    print(f"   - Posição em t = {t_final}s: r({t_final}) = {posicao_t2[0]} î + {posicao_t2[1]} ĵ (em cm)")

    print("\n2. Velocidade Média:")
    if isinstance(v_media, np.ndarray):
        print(f"   - No intervalo [{t_inicial}s, {t_final}s]: v_med = {v_media[0]} î + {v_media[1]} ĵ (em cm/s)")
    else:
        print(f"   - {v_media}")

    print("\n3. Velocidade Instantânea:")
    print(f"   - Em t = {t_inicial}s: v({t_inicial}) = {velocidade_t0[0]} î + {velocidade_t0[1]} ĵ (em cm/s)")
    print(f"   - Em t = {t_final}s: v({t_final}) = {velocidade_t2[0]} î + {velocidade_t2[1]} ĵ (em cm/s)")