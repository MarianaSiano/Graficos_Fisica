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

#--- SEÇÃO DE EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    t_inicial = 0.0
    t_final = 2.0

    print(f"--- ANÁLISE CINEMÁTICA PARA O INTERVALO DE t = {t_inicial}s a t = {t_final}s ---")

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
    print(f"   - Posição em t = {t_inicial}s: r({t_inicial}) = {posicao_t0[0]:.1f} î + {posicao_t0[1]:.1f} ĵ (em cm)")
    print(f"   - Posição em t = {t_final}s: r({t_final}) = {posicao_t2[0]:.1f} î + {posicao_t2[1]:.1f} ĵ (em cm)")

    print("\n2. Velocidade Média:")
    if isinstance(v_media, np.ndarray):
        print(f"   - Vetor no intervalo [{t_inicial}s, {t_final}s]: v_med = {v_media[0]:.1f} î + {v_media[1]:.1f} ĵ (em cm/s)")
        print(f"   - Módulo: {modulo_media:.2f} cm/s")
        print(f"   - Direção e Sentido: {angulo_media:.2f}° (em relação ao eixo x positivo)")
    else:
        print(f"   - {v_media}")

    print("\n3. Velocidade Instantânea:")
    print(f"   - Em t = {t_inicial}s: v({t_inicial}) = {velocidade_t0[0]:.1f} î + {velocidade_t0[1]:.1f} ĵ (em cm/s)")
    print(f"     - Módulo: {modulo_t0:.2f} cm/s")
    print(f"     - Direção e Sentido: {angulo_t0}° (em relação ao eixo x positivo)")
    
    print(f"\n   - Em t = {t_final}s: v({t_final}) = {velocidade_t2[0]:.1f} î + {velocidade_t2[1]:.1f} ĵ (em cm/s)")
    print(f"     - Módulo: {modulo_t2:.2f} cm/s")
    print(f"     - Direção e Sentido: {angulo_t2:.2f}° (em relação ao eixo x positivo)")

    print(f"\n--- Gerando o gráfico ---")

    #Gera 100 pontos para a curva da trajetória
    t_valores = np.linspace(t_inicial, t_final, 100)
    trajetoria = np.array([calcular_vetor_posicao(t) for t in t_valores])

    #--- Criação do Gráfico Final e Explicativo
    fig, ax = plt.subplots(figsize=(14, 10))

    #1.Desenhar a Trajetória
    ax.plot(trajetoria[:, 0], trajetoria[:, 1], 
            color='black', 
            linewidth=2, 
            linestyle='--',
            label='Trajetória')

    #2. Plotar os vetores de POSIÇÃO e DESLOCAMENTO
    ax.arrow(0, 0, posicao_t0[0], posicao_t0[1], head_width=0.3, fc='#9370DB', ec='#9370DB', length_includes_head=True, label='r(0): Posição Inicial')
    ax.arrow(0, 0, posicao_t2[0], posicao_t2[1], head_width=0.3, fc='#66CDAA', ec='#66CDAA', length_includes_head=True, label='r(2): Posição Final')
    ax.arrow(posicao_t0[0], posicao_t0[1], delta_r[0], delta_r[1], head_width=0.3, fc='#FF4500', ec='#FF4500', length_includes_head=True, label='Δr: Deslocamento')
    
    #3. Plotar os vetores de VELOCIDADE INSTANTÂNEA
    #Vetor v(0) partindo do ponto r(0)
    ax.arrow(posicao_t0[0], posicao_t0[1], velocidade_t0[0], velocidade_t0[1], head_width=0.4, fc='#0000CD', ec='#0000CD', length_includes_head=True, label='v(0): Velocidade em t=0s')
    #Vetor v(2) partindo do ponto r(2)
    ax.arrow(posicao_t2[0], posicao_t2[1], velocidade_t2[0], velocidade_t2[1], head_width=0.4, fc='#00CED1', ec='#00CED1', length_includes_head=True, label='v(2): Velocidade em t=2s')


    #4. Configurações do gráfico
    ax.set_title("Análise Cinemática do Ponto", fontsize=18)
    ax.set_xlabel('Posição X (cm)', fontsize=14)
    ax.set_ylabel('Posição Y (cm)', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    #Adiciona a origem para referência
    ax.plot(0, 0, 'ko') # Ponto na origem
    ax.text(0, -0.8, 'Origem', ha='center')
    
    #Garante que a forma da curva não seja distorcida
    ax.set_aspect('equal', adjustable='box') 
    
    #Ajusta os limites para todos os vetores serem visíveis
    plt.xlim(-2, 26)
    plt.ylim(-2, 17)

    plt.show()