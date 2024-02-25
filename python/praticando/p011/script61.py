# Solicite ao usuário um valor inteiro
numero = int(input("Digite um valor inteiro: "))

# Variável para armazenar o dígito atual
digito_atual = 9  # Começamos com 9, pois é o maior dígito possível

# Variável para armazenar os dígitos em ordem crescente
ordem_crescente = ""

# Processo para encontrar os dígitos em ordem crescente
while numero > 0:
    # Encontre o dígito atual
    resto = numero % 10
    
    # Verifique se o dígito atual é maior ou igual ao último dígito encontrado
    if resto <= digito_atual:
        ordem_crescente = str(resto) + ordem_crescente
        digito_atual = resto
    else:
        pass
    # Reduza o número removendo o último dígito
    numero = numero // 10

# Imprima os dígitos em ordem crescente
print("Dígitos em ordem crescente:", ordem_crescente)
