# Faça um programa que mostre a tabuada de vários númeors, um de cada vez, para cada valor digitado. O programa será interrompido quando o número solicitado for negativo.

def menu ():
    print("DIGITE VALORES PARA EXIBIR A TABUADA. \nSENDO NEGATIVO O PROGRAMA IRÁ ENCERRAR.")

def verificarNegativo (n):
    if n < 0:
        return True
    else:
        return False

 
def main ():
    menu()

    while True:
        num = int(input("Digite o valor: "))
        
        if verificarNegativo(num):
            break
        else:
            for i in range (1, 11):
                print(f'{i} X {num} = {i*num}')
        
    print("Até mais...")


main()
