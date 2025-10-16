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
    
    #--- Exemplo 1: Cálculo da Velocidade Média ---
    print("--- CÁLCULO DA VELOCIDADE MÉDIA ---")
    t_inicial = 0.0
    t_final = 2.0

    try:
        #Calcula as posições para exibição
        posicao_inicial = calcular_vetor_posicao(t_inicial)
        posicao_final = calcular_vetor_posicao(t_final)
        
        #Calcula a velocidade média
        v_media = calcular_velocidade_media(t_inicial, t_final)

        #Imprime os resultados
        print(f"Intervalo de tempo: de t = {t_inicial}s até t = {t_final}s")
        print(f"Posição inicial r({t_inicial}) = {posicao_inicial[0]} î + {posicao_inicial[1]} ĵ cm")
        print(f"Posição final   r({t_final}) = {posicao_final[0]} î + {posicao_final[1]} ĵ cm")
        print("-" * 25)
        print(f"Velocidade média = {v_media[0]} î + {v_media[1]} ĵ (em cm/s)")

    except ValueError as e:
        print(f"Erro no cálculo: {e}")

    print("\n" + "="*40 + "\n")

    #--- Exemplo 2: Cálculo da Velocidade Instantânea ---
    print("--- CÁLCULO DA VELOCIDADE INSTANTÂNEA ---")
    
    #Podemos usar o mesmo tempo final do exemplo anterior para comparar
    tempo_instantaneo = 2.0

    #Calcula a velocidade instantânea
    v_instantanea = calcular_velocidade_instantanea(tempo_instantaneo)

    #Imprime os resultados
    print(f"Instante de tempo: t = {tempo_instantaneo}s")
    print("-" * 25)
    print(f"Velocidade instantânea v({tempo_instantaneo}) = {v_instantanea[0]} î + {v_instantanea[1]} ĵ (em cm/s)")