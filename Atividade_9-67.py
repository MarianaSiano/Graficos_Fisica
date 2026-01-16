import numpy as np
import matplotlib.pyplot as plt

# 1. Definiçãp dos parâmetros físicos
R = 0.25 # Raio do disco em metros (25cm)
A = 0.60 # Constante calculada no item (a)

# 2. Criação do vetor
# Simular de 0 a 4 s para cobrir o instante de interesse (aprox. 3.54s)
t = np.linspace(0, 4, 200)

# 3. Equações do movimento (Escritas explicitamente)

# Aceleração angular: alpha(t) = 2.40t
# (Derivado de: alpha = At/R = 0.60t/0.25)
alpha = 2.40 * t

# Velocidade angular: omega(t) = 1.20t^2
# (Derivado de: integral de 2.40t)
omega = 1.20 * t ** 2

# Posição angular: theta(t) = 0.40t^3
# (Derivado de: integral de 1.20t^2)
theta = 0.40 * t ** 3