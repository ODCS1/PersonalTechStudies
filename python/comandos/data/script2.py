import numpy as np
import pandas as pd

lista = [1, 2, 3, 4, 5, 6]

vetor = np.array(lista)

matriz = vetor.reshape(2, 3)
# matriz = vetor.reshape(2, -1)

# print("Vetor Original: \n" + str(vetor))
# print("\nMatriz 2x3: \n" + str(matriz))


dados_sensores = [22.4, 24.6, 21.9, 23, 22.7, 21.5]
# temperatuda, umidade e pressão

matriz_sensores = np.array(dados_sensores).reshape(-1, 3)
# print(matriz_sensores)

data = {
    'temperatura': matriz_sensores[:, 0],
    'umidade': matriz_sensores[:, 1],
    'pressao': matriz_sensores[:, 2]
}
# print(data)

df = pd.DataFrame(data)
print(df)