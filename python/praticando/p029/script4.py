import numpy as np

class Simplex:
    def __init__(self, c, A, b):
        """
        Inicializa o problema de programação linear na forma padrão:
        Minimizar c^T * x
        Sujeito a A * x >= b
        onde x >= 0
        """
        self.c = np.array(c, dtype=float)  # Coeficientes da função objetivo a ser minimizada
        self.A = np.array(A, dtype=float)  # Coeficientes das restrições
        self.b = np.array(b, dtype=float)  # Termos independentes das restrições
        
        self.m, self.n = self.A.shape  # m = número de restrições, n = número de variáveis
        
        # Verifica se o número de variáveis na função objetivo é consistente com A
        if self.n != len(self.c):
            raise ValueError("Dimensões inconsistentes: A e c não têm o mesmo número de colunas")
        
        # Verifica se o número de restrições é consistente com b
        if self.m != len(self.b):
            raise ValueError("Dimensões inconsistentes: A e b não têm o mesmo número de linhas")
        
        # Inicializa o tableau simplex
        self.tableau = np.zeros((self.m + 1, self.n + self.m + 1))
        self.tableau[:-1, :-1] = np.hstack([self.A, np.eye(self.m)])
        self.tableau[:-1, -1] = self.b
        self.tableau[-1, :-1] = -self.c
        
        # Índices das variáveis básicas e não básicas
        self.basic_vars = np.arange(self.n, self.n + self.m)
        self.nonbasic_vars = np.arange(self.n)
        
    def solve(self):
        """
        Resolve o problema de programação linear usando o método simplex.
        Retorna a solução ótima e o valor da função objetivo mínima.
        """
        while self.tableau[-1, :-1].min() < 0:
            # Escolhe a coluna pivot (variável não básica que entra na base)
            entering_var = np.argmin(self.tableau[-1, :-1])
            
            # Verifica se a solução é ilimitada
            if np.all(self.tableau[:-1, entering_var] <= 0):
                raise ValueError("O problema é ilimitado")
            
            # Escolhe a linha pivot usando a regra da razão mínima
            ratios = self.tableau[:-1, -1] / self.tableau[:-1, entering_var]
            ratios[ratios < 0] = np.inf  # Evita divisão por zero quando o elemento é negativo
            leaving_var = np.argmin(ratios)
            
            # Atualiza a base
            self.basic_vars[leaving_var] = entering_var
            
            # Pivoteia
            pivot_row = self.tableau[leaving_var, :]
            self.tableau = self.tableau - np.outer(self.tableau[:, entering_var], pivot_row) / pivot_row[entering_var]
        
        # Extrai a solução e o valor da função objetivo mínima
        solution = np.zeros(self.n)
        for i in range(self.m):
            if self.basic_vars[i] < self.n:
                solution[self.basic_vars[i]] = self.tableau[i, -1]
        
        min_value = -self.tableau[-1, -1]  # Valor da função objetivo mínima
        
        return solution, min_value

# Exemplo de uso:
if __name__ == "__main__":
    c = [5, 1]
    A = [[2, 1],
         [1, 1],
         [1, 5]]
    b = [6, 4, 10]
    
    simplex = Simplex(c, A, b)
    solution, min_value = simplex.solve()
    
    print("Solução ótima encontrada:")
    print(f"x1 = {solution[0]}, x2 = {solution[1]}")
    print(f"Valor mínimo da função objetivo: {min_value}")
