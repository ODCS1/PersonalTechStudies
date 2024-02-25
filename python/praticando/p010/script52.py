def mascara_e_intervalo(endereco_ip, prefixo_rede):
    # Converte o endereço IP para uma lista de números inteiros
    ip = [int(x) for x in endereco_ip.split('.')]
    
    # Calcula a máscara de sub-rede
    mascara = [0, 0, 0, 0]
    for i in range(prefixo_rede):
        mascara[i//8] += 1 << (7 - i % 8)
    
    # Calcula o endereço de rede
    endereco_rede = [ip[i] & mascara[i] for i in range(4)]
    
    # Calcula o primeiro endereço disponível para hosts
    primeiro_endereco = endereco_rede.copy()
    primeiro_endereco[3] += 1
    
    # Calcula o último endereço disponível para hosts
    ultimo_endereco = endereco_rede.copy()
    ultimo_endereco[3] = (ultimo_endereco[3] | ~mascara[3]) & 255
    
    # Converte as listas de números inteiros para uma string de IP
    mascara_str = '.'.join(str(x) for x in mascara)
    intervalo_str = '.'.join(str(x) for x in primeiro_endereco) + ' - ' + '.'.join(str(x) for x in ultimo_endereco)
    
    # Exibe a máscara de sub-rede e o intervalo de IPs
    print("Máscara de sub-rede:", mascara_str)
    print("Intervalo de IPs disponíveis:", intervalo_str)

# Exemplo de uso
mascara_e_intervalo("197.216.114.64", 28)
