import pandas as pd
import numpy as np

dados_sensores = [21.5, 22.3, 24.6, 23.4, 20.5, 22.5, 25.3, 24.2, 20.5]
# temperatura, umidade, pressão

matriz_sensores = np.array(dados_sensores).reshape(int(len(dados_sensores) / 3), 3)

# print(matriz_sensores)

df = pd.DataFrame(
    {
        'temperatura': matriz_sensores[:, 0],
        'umidade': matriz_sensores[:, 1],
        'pressao': matriz_sensores[:, 2]
    }
)

print(df)