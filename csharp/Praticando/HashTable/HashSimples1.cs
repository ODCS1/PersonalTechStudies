using System;

public class HashSimples1 {
    const int tamanhoPadrao = 10007;
    string[] tabela;

    public HashSimples1 () : this(tamanhoPadrao) {}
    public HashSimples1 (int tamanho){
        string[] tabela = new string[tamanho];
    }

    public int Hash(string chave){
        int tot = 0;
        for(int i = 0; i < tabela.Length; i++){
            tot += (int) chave[i];
        }
        return tot % tabela.Length;
    }

    public string Incluir(string chave){
        string saida = "";
        int valorHash = Hash(chave);
        if(tabela[valorHash] == null){
            
            tabela[valorHash] = chave;
            return saida;
        }

        saida = $"Houve colisão entre o valor {chave} e o valor já armazenado {tabela[valorHash]} na posição {valorHash}."

        return saida;
    }

    public bool Existe(string chave, out int posicao){
        posicao = Hash(chave);
        return chave == tabela[posicao];
    }

    public List<string> Conteudo(){
        var saida = new List<>();

        for (int i = 0; i < tabela.Length; i++){
            if (tabela[i] != null){
                saida.Add($"{i} : {tabela[i]}");
            }else{
                saida.Add($"{i} : {null}");
            }
        }
        return saida;
    }

    public void Limpar(){
        for(int i = 0; i < tabela.Length; i++){
            tabela[i] = null;
        }
    }
}