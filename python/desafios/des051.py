# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 110 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o 1° termo de uma P.A.: '))
razao = int(input('Digite agora a razão dessa P.A.: '))

termo_atual = primeiro_termo - razao
cont = 1
while cont <= 110:
    termo_atual += razao
    print(f'{cont}° termo: {termo_atual}')
    cont += 1