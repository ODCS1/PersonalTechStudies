# 1. Escreva uma função em Python que, dado o código de um curso, bem como a lista de 
# cursos, resulte a duração dele, caso esteja cadastrado, ou None, caso contrário. Faça um 
# programa para testar sua função.



def program(cod: int, curso: list[dict]) -> int:
    if not(isinstance(cod, int)):
        raise ValueError("Tipo de parâmetro Inválido!")


    for c in curso:
        if c["Codigo"] == cod:
            return c["Duracao"]
    
    return None



def main():
    try:
        Curso = [
            {"Codigo":123,"Nome":"Sistemas de Informação","Duracao":4},
            {"Codigo":213,"Nome":"Ciência de Dados e IA","Duracao":4},
            {"Codigo":321,"Nome":"Engenharia Biomédica","Duracao":5}
        ]

        
        codCurso = 213

        duracao_curso = program(codCurso, Curso)

        if duracao_curso is not None: print(f"A duração do curso é de {duracao_curso} anos!")
        else: print("Não foi passado um código de curso existente.")

        
    except ValueError as e:
        print(f"[ERRO] {e}")





if __name__ == "__main__": main()