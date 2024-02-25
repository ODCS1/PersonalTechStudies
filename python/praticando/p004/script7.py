clientes = {}

comandas_abertas = []


# Função Principal

def main():
    while True:
        print("Menu de opções:")
        print("1. Cadastrar novo cliente")
        print("2. Abrir comanda")
        print("3. Fazer um pedido")
        print("4. Fechar comanda")
        print("5. Ver comandas abertas")
        print("6. Ver clientes cadastrados")
        print("7. Ver valor da comanda aberta")
        print("8. Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            abrir_comanda()
        elif opcao == "3":
            fazer_pedido()
        elif opcao == "4":
            fechar_comanda()
        elif opcao == "5":
            ver_comandas_abertas()
        elif opcao == "6":
            ver_clientes_cadastrados()
        elif opcao == "7":
            ver_valor_comanda_aberta()
        elif opcao == "8":
            sair()
        else:
            print("Opção inválida.")


# Cadastrar novo cliente

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    clientes[telefone] = nome
    print("Cliente cadastrado com sucesso!")

# Abrir comanda

def abrir_comanda():
    telefone = input("Digite o número do telefone do cliente: ")
    if telefone in clientes:
        comandas_abertas.append({
            "telefone": telefone,
            "pedidos": [],
            "valor_total": 0
        })
        print("Comanda aberta com sucesso!")
    else:
        print("Cliente não encontrado.")


# Fazer um pedido

def fazer_pedido():
    telefone = input("Digite o número do telefone do cliente: ")
    comanda = None
    for c in comandas_abertas:
        if c["telefone"] == telefone:
            comanda = c
            break
    if comanda is None:
        print("Comanda não encontrada.")
        return
    print("Menu de bebidas:")
    print("1. Cerveja (R$5)")
    print("2. Refrigerante (R$4)")
    print("3. Suco (R$3)")
    opcao = input("Digite o número da bebida desejada: ")
    if opcao == "1":
        bebida = "Cerveja"
        valor = 5
    elif opcao == "2":
        bebida = "Refrigerante"
        valor = 4
    elif opcao == "3":
        bebida = "Suco"
        valor = 3
    else:
        print("Opção inválida.")
        return
    comanda["pedidos"].append({
        "bebida": bebida,
        "valor": valor
    })
    comanda["valor_total"] += valor
    print("Pedido adicionado com sucesso!")

# Fechar comanda

def fechar_comanda():
    telefone = input("Digite o número do telefone do cliente: ")
    comanda = None
    for c in comandas_abertas:
        if c["telefone"] == telefone:
            comanda = c
            break
    if comanda is None:
        print("Comanda não encontrada.")
        return
    print("Comanda do cliente", clientes[telefone])
    for pedido in comanda["pedidos"]:
        print(pedido["bebida"], "- R$", pedido["valor"])
    print("Valor total: R$", comanda["valor_total"])
    comandas_abertas.remove(comanda)
    print("Comanda fechada com sucesso!")


# Ver comandas abertas

def ver_comandas_abertas():
    for c in comandas_abertas:
        print("Comanda do cliente", clientes[c["telefone"]])
        for pedido in c["pedidos"]:
            print(pedido["bebida"], "- R$", pedido["valor"])
        print("Valor total: R$", c["valor_total"])


# Ver clientes cadastrados

def ver_clientes_cadastrados():
    for telefone, nome in clientes.items():
        print(nome, "-", telefone)


# Ver valor da comanda aberta

def ver_valor_comanda_aberta():
    telefone = input("Digite o número do telefone do cliente: ")
    comanda = None
    for c in comandas_abertas:
        if c["telefone"] == telefone:
            comanda = c
            break
    if comanda is None:
        print("Comanda não encontrada.")
        return
    print("Valor total da comanda:", comanda["valor_total"])


# Sair do sistema

def sair():
    print("Saindo do sistema...")
    exit()

# Chamar a função main() para iniciar o sistema

if __name__ == "__main__":
    main()
