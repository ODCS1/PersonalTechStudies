using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class HashSimples
{
    const int tamanhoPadrao = 10007;
    string[] tabelaDeHash;
    public HashSimples() : this(tamanhoPadrao) { }
    
    public HashSimples(int tamanhoDesejado)
    {
        tabelaDeHash = new string[tamanhoDesejado];
    }
    private int Hash(string chave)
    {
        int tot = 0;
        for (int i = 0; i < chave.Length; i++)
            tot += (int)chave[i];
        return tot % tabelaDeHash.Length;
    }
    
    public string Incluir(string chave)
    {
        string saida = "";
        int valorDeHash = Hash(chave.Trim()); // posicao calculada para um registro
        if (tabelaDeHash[valorDeHash] != null) // já há dado armazenado nessa posição
            saida = $"colisao na posicao {valorDeHash} entre " +
            $"{tabelaDeHash[valorDeHash]} e {chave}";
        tabelaDeHash[valorDeHash] = chave;
        return saida;
    }
    
    public bool Existe(string s, out int posicao)
    {
        posicao = Hash(s);
        return tabelaDeHash[posicao] == s;
    }
    
    public List<string> Conteudo()
    {
        var saida = new List<string>();
        for (int i = 0; i < tabelaDeHash.Length; i++)
            if (tabelaDeHash[i] != null)
                saida.Add($"{i,5} : {tabelaDeHash[i]}");
            //else
            // saida.Add($"{i} ");
            return saida;
    }
    
    public void Limpar()
    {
        for (int i = 0; i < tabelaDeHash.Length; i++)
            tabelaDeHash[i] = null;
    }
}

// Este código implementa uma tabela de dispersão simples (hash table) em C#. Aqui está uma explicação detalhada do código:

// Declaração de HashSimples class: A classe HashSimples contém métodos para manipular uma tabela de dispersão.

// Constante tamanhoPadrao: Define um tamanho padrão para a tabela de dispersão. O valor padrão é 10007.

// Declaração de tabelaDeHash: Um array de strings que é usado como a própria tabela de dispersão.

// Construtor HashSimples(): Este construtor chama o construtor HashSimples(int tamanhoDesejado) com o tamanho padrão.

// Construtor HashSimples(int tamanhoDesejado): Este construtor inicializa a tabelaDeHash com o tamanho especificado.

// Método Hash(string chave): Este método calcula o valor de hash para uma determinada chave. Ele soma os valores ASCII dos caracteres da chave e, em seguida, retorna o resto da divisão desse total pelo tamanho da tabela de hash.

// Método Incluir(string chave): Este método insere uma chave na tabela de dispersão. Ele primeiro calcula o valor de hash da chave e verifica se há uma colisão (ou seja, se outra chave já está armazenada na mesma posição). Se houver uma colisão, ele retorna uma mensagem indicando a colisão. Caso contrário, ele insere a chave na posição calculada na tabela de dispersão.

// Método Existe(string s, out int posicao): Este método verifica se uma determinada chave está presente na tabela de dispersão. Ele calcula o valor de hash da chave e verifica se o elemento na posição correspondente é igual à chave. Ele retorna true se a chave estiver presente e false caso contrário. Além disso, ele retorna a posição da chave na tabela de dispersão através do parâmetro de saída posicao.

// Método Conteudo(): Este método retorna uma lista de strings representando o conteúdo da tabela de dispersão. Ele itera sobre cada posição da tabela de dispersão e adiciona a posição e o valor correspondente à lista de saída. Note que há um erro de indentação aqui, o return saida; está dentro do loop for, o que fará com que apenas o primeiro elemento seja verificado e o método retorne imediatamente.

// Método Limpar(): Este método limpa a tabela de dispersão, atribuindo null a cada posição.

// Em resumo, este código implementa uma tabela de dispersão simples em C# com métodos para adicionar, verificar a existência, listar o conteúdo e limpar a tabela. No entanto, é importante corrigir o erro de indentação no método Conteudo() para garantir que ele funcione corretamente.