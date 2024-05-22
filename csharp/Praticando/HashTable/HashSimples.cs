using System;

public class HashSimples {
    const int tamanhoPadrao = 10007;
    string[] tabela;
    
    public HashSimples(int tamanho){
        string[] tabela = new string[tamanho];
    }

    public HashSimples() : this(tamanhoPadrao) {}

    public int Hash(string chave){
        int tot = 0;
        for(int i = 0; i < chave.Length; i++){
            int tot += (int) chave[i]
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

        saida = $"Conflito entre {chave} e valor já armazenado {tabela[valorHash]} na posição {valorHash}."

        return saida;
    }

    public bool Existe(string chave, out int posicao){
        posicao = Hash(chave);
        return tabela[posicao] == chave;
    }

    public List<string> Conteudo(){
        var saida = new List<string>();

        for (int i = 0; i < tabela.Length; i++){
            if(tabela[i] != null){
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