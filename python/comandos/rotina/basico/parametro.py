# Para fazer a passagem de parâmetro é simples, apenas deve ser colcoado o valor ou variável que deseja fazer a passagem.

def funcao(x, y):
    return x + y

a = 2
b = 3
resultado = funcao(a, b)
print(f'O resultado entre {a} + {b} = {resultado}.')

# Ou eu poderia simplesmente passar o valor direto, mas esse é um caso muito específico que não é utilizado, pois se eu já sei quais valores serão passados, eu simplesmente os utilizo já dentro da função, seja definindo em variáveis próprias ou dentro de outras variáveis que necessite desses valores.

# Exemplo:

def outraFuncao(w, z):
    return w + z

print(f'Resultado da outraFunção, 1 + 3 = {outraFuncao(1, 3)}.')