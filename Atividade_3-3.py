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
        return modulo, "Indefinida"
    angulo_rad = math.atan2(vetor[1], vetor[0])
    angulo_graus = math.degrees(angulo_rad)
    return modulo, angulo_graus

#--- SEÇÃO DE EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    t_inicial = 0.0
    t_final = 2.0

    print(f"--- ANÁLISE CINEMÁTICA PARA O INTERVALO DE t={t_inicial}s a t={t_final}s ---")

    #--- Cálculos ---
    posicao_t0 = calcular_vetor_posicao(t_inicial)
    posicao_t2 = calcular_vetor_posicao(t_final)
    delta_r = posicao_t2 - posicao_t0
    
    try:
        v_media = calcular_velocidade_media(t_inicial, t_final)
        modulo_media, angulo_media = analisar_vetor(v_media)
    except ValueError as e:
        v_media = f"Erro: {e}"
        modulo_media, angulo_media = "-", "-"

    velocidade_t0 = calcular_velocidade_instantanea(t_inicial)
    velocidade_t2 = calcular_velocidade_instantanea(t_final)
    modulo_t0, angulo_t0 = analisar_vetor(velocidade_t0)
    modulo_t2, angulo_t2 = analisar_vetor(velocidade_t2)

    #--- Exibição dos resultados em texto ---
    print("\n1. Posição:")
    print(f"   - Posição em t = {t_inicial}s: r({t_inicial}) = {posicao_t0[0]} î + {posicao_t0[1]} ĵ (em cm)")
    print(f"   - Posição em t = {t_final}s: r({t_final}) = {posicao_t2[0]} î + {posicao_t2[1]} ĵ (em cm)")

    print("\n2. Velocidade Média:")
    if isinstance(v_media, np.ndarray):
        print(f"   - Vetor no intervalo [{t_inicial}s, {t_final}s]: v_med = {v_media[0]} î + {v_media[1]} ĵ (em cm/s)")
        print(f"   - Módulo: {modulo_media:.2f} cm/s")
        print(f"   - Direção e Sentido: {angulo_media:.2f}° (em relação ao eixo x positivo)")
    else:
        print(f"   - {v_media}")

    print("\n3. Velocidade Instantânea:")
    print(f"   - Em t = {t_inicial}s: v({t_inicial}) = {velocidade_t0[0]} î + {velocidade_t0[1]} ĵ (em cm/s)")
    print(f"     - Módulo: {modulo_t0:.2f} cm/s")
    print(f"     - Direção e Sentido: {angulo_t0}° (em relação ao eixo x positivo)")
    
    print(f"\n   - Em t = {t_final}s: v({t_final}) = {velocidade_t2[0]} î + {velocidade_t2[1]} ĵ (em cm/s)")
    print(f"     - Módulo: {modulo_t2:.2f} cm/s")
    print(f"     - Direção e Sentido: {angulo_t2:.2f}° (em relação ao eixo x positivo)")

    #--- Criação do Gráfico ---
    print("\n--- Gerando gráfico de soma vetorial... ---")
    
    fig, ax = plt.subplots(figsize=(10, 8))

    #1. Plotar o vetor posição inicial r(0)
    ax.arrow(0, 0, posicao_t0[0], posicao_t0[1], 
            head_width=0.4, head_length=0.5, fc='purple', ec='purple', 
            length_includes_head=True, label='Vetor Posição Inicial r(0)')

    #2. Plotar o vetor deslocamento Δr
    ax.arrow(posicao_t0[0], posicao_t0[1], delta_r[0], delta_r[1],
            head_width=0.4, head_length=0.5, fc='red', ec='red', 
            length_includes_head=True, label='Vetor Deslocamento Δr = r(2) - r(0)')
    
    #3. Plotar o vetor posição final r(2)
    ax.arrow(0, 0, posicao_t2[0], posicao_t2[1],
            head_width=0.4, head_length=0.5, fc='black', ec='black', 
            length_includes_head=True, label='Vetor Posição Final r(2) = r(0) + Δr')
    
    #4. Desenhar a trajetória real
    t_valores = np.linspace(t_inicial, t_final, 100)
    trajetoria = np.array([calcular_vetor_posicao(t) for t in t_valores])
    ax.plot(trajetoria[:, 0], trajetoria[:, 1], color='gray', linestyle='--', label='Trajetória Real da Partícula')

    #5. Marcar os pontos
    ax.plot(0, 0, 'o', color='black', markersize=5, label='Origem (0,0)')
    ax.plot(posicao_t0[0], posicao_t0[1], 'o', color='purple', markersize=7)
    ax.plot(posicao_t2[0], posicao_t2[1], 'o', color='black', markersize=7)

    #6. Configurações do gráfico
    ax.set_title('Soma Vetorial: r(2) = r(0) + Δr', fontsize=16)
    ax.set_xlabel('Posição X (cm)', fontsize=12)
    ax.set_ylabel('Posição Y (cm)', fontsize=12)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    
    plt.xlim(-1, 16)
    plt.ylim(-1, 12)

    plt.show()