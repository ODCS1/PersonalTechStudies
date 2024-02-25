# 3 - Contagem de Palavras em um Texto: Crie um programa que conte o número de palavras em um texto fornecido como entrada.


def contador(txt):
    txtSepara = txt.split()
    tam = len(txtSepara)

    return f"QUANTIDADE DE PALAVRAS: {tam}."


txt = "palavra no texto, assim sendo."

print(contador(txt))