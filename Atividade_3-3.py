import numpy as np

def calcular_vetor_posicao(t: float) -> np.ndarray:
    """
    Calcula o vetor posição r(t) para um dado tempo t.

    A equação do vetor é: r(t) = [4.0 + (2.5 * t^2)]î + (5.0 * t)ĵ

    Args:
        t (float): O tempo em segundos (s).

    Returns:
        numpy.ndarray: Um array NumPy representando o vetor posição [x, y] em cm.
    """
    # Componente x do vetor
    x = 4.0 + (2.5 * (t ** 2))

    #Componente y do vetor
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
        numpy.ndarray: Um array NumPy representando o vetor velocidade média [vx, vy] em cm/s.
    
    Raises:
        ValueError: Se t1 e t2 forem iguais, para evitar divisão por zero.
    """
    #Calcula a variação do tempo
    delta_t = t2 - t1

    #Validação para evitar divisão por zero
    if delta_t == 0:
        raise ValueError("O tempo inicial (t1) e final (t2) não podem ser iguais.")

    #Calcula as posições e a variação
    r1 = calcular_vetor_posicao(t1)
    r2 = calcular_vetor_posicao(t2)
    delta_r = r2 - r1
    
    #Calcula o vetor velocidade média
    velocidade_media = delta_r / delta_t
    return velocidade_media

def calcular_velocidade_intantanea(t: float) -> np.ndarray:
    """
    Calcula o vetor velocidade instantânea v(t) para um dado tempo t.

    A equação é a derivada do vetor posição: v(t) = (5.0 * t)î + 5.0ĵ

    Args:
        t (float): O tempo em segundos (s) no qual a velocidade será calculada.

    Returns:
        numpy.ndarray: Um array NumPy representando o vetor velocidade [vx, vy] em cm/s.
    """

#--- Seção de Execução Principal ---
if __name__ == "__main__":
    # Definição do intervalo de tempo
    t_inicial = 0.0  #em segundos
    t_final = 2.0    #em segundos

    try:
        #--- Calculamos as posições aqui para poder usá-las no print ---
        posicao_inicial = calcular_vetor_posicao(t_inicial)
        posicao_final = calcular_vetor_posicao(t_final)

        #Chama a função para calcular a velocidade média
        v_media = calcular_velocidade_media(t_inicial, t_final)

        #--- Impressão dos Resultados ---
        print(f"Calculando a velocidade média entre t = {t_inicial}s e t = {t_final}s:")
        
        #--- CORREÇÃO: Usamos as variáveis definidas acima (posicao_inicial e posicao_final) ---
        print(f"Vetor posição em t1 = {t_inicial}s: r({t_inicial}) = {posicao_inicial[0]} î + {posicao_inicial[1]} ĵ cm")
        print(f"Vetor posição em t2 = {t_final}s: r({t_final}) = {posicao_final[0]} î + {posicao_final[1]} ĵ cm")
        
        print("-" * 40)
        print("Resultado:")
        print(f"O vetor velocidade média é: v_med = {v_media[0]} î + {v_media[1]} ĵ (em cm/s)")

    except ValueError as e:
        print(f"Erro no cálculo: {e}")