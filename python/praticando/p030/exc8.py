# 1 - Validação de Senha: Crie um programa que solicite ao usuário que crie uma senha. A senha deve atender aos seguintes critérios: ter pelo menos 8 caracteres, conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O programa deve validar se a senha atende a esses critérios.

def validarSenha (senha):
    contCriterios = 0

    if " " in senha:
        pass
    else:
        if len(senha) > 7:
            contCriterios += 1
        existeMaiusc = False
        existeMinusc = False
        existeNum = False
        for i in range(len(senha)):
            if senha[i].isupper():
                existeMaiusc = True
            elif senha[i].islower():
                existeMinusc = True
            else:
                existeNum = True

            if existeMinusc and existeMaiusc and existeNum:
                break

        if existeMaiusc and existeMinusc and existeNum:
            contCriterios += 3
        
    if contCriterios >= 4:
        print("A SENHA É VÁLIDA!")
    else:
        print("A SENHA NÃO É VÁLIDA!!!")


def formatar ():
    print('-'*40)
    print("|{}{:^38}{}|".format("\033[31m", "VERIFICADOR", "\033[m"))
    print('-'*40)
    print("\tDigite uma senha {}VÁLIDA!!!{}\n".format("\033[34m", "\033[m"))
    print("Deve ter pelo menos 8 caracteres, contendo pelo menos 1 letra maiúscula, uma minúscula e um número.\n")

def main ():
    formatar()
    senha = input("Digite a senha: ")
    validarSenha(senha)


main()
