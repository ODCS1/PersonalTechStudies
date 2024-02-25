def mascaraEintervalo(endereco_ip, prefixo_rede):
    # Calcula a máscara de sub-rede
    mascara_bin = '1' * prefixo_rede + '0' * (32 - prefixo_rede)
    mascara = [int(mascara_bin[i:i+8], 2) for i in range(0, 32, 8)]
    
    # Calcula o endereço de rede
    endereco_rede = [int(endereco_ip.split('.')[i]) & mascara[i] for i in range(4)]
    
    # Calcula o primeiro endereço disponível para hosts
    primeiro_endereco = endereco_rede.copy()
    primeiro_endereco[3] += 1
    
    # Calcula o último endereço disponível para hosts
    ultimo_endereco = endereco_rede.copy()
    ultimo_endereco[3] = endereco_rede[3] + 2 ** (32 - prefixo_rede) - 2
    
    # Converte as listas de números inteiros para uma string de IP
    mascara_str = '.'.join(str(x) for x in mascara)
    intervalo_str = '.'.join(str(x) for x in primeiro_endereco) + ' - ' + '.'.join(str(x) for x in ultimo_endereco)
    
    # Exibe a máscara de sub-rede e o intervalo de IPs
    print(f'Máscara de sub-rede: {mascara_str} \nIntervalo de IPs disponíveis: {intervalo_str}')

# chamada da função
mascaraEintervalo("197.216.114.64", 28)