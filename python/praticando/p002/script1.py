frase = ' Curso em Video Python '

print('Contador de o: ', frase.count('o'))
print('Contador de O: ', frase.upper().count('O'))
print('Tamanho: ', len(frase))
print("Tamanho com strip: ", len(frase.strip()))
print("Tamanho com rstrip: ", len(frase.rstrip()))
print("Tamanho com ltrip: ", len(frase.lstrip()))
print('Trocando python por android: ', frase.replace('Python', 'Android'))
print('Testando se a palavra Curso está na frase: ', 'Curso' in frase)
print('Procurando a posição da palavra Curso: ', frase.find('Curso'))
print('Deixando a posição 0 Maiúsculo: ', frase.capitalize())
print('Deixando os inicios Maiusc: ', frase.title())
print('')

dividido = frase.split()
print('Dividido(split): ', dividido)
print('Dividido posição 0: ', dividido[0])
print('Dividido posição [0][0]: ', dividido[0][0])

dividido = '-'.join(dividido)
print('Divididido(join): ', dividido)