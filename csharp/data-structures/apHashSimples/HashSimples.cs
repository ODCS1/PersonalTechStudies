using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


    public class HashSimples
    {
        const int tamanhoPadrao = 10007;
        string[] tabelaDeHash;


        public HashSimples(int tamanhoDesejado)
        {
        tabelaDeHash = new string[tamanhoDesejado];
        }

        public HashSimples(): this(tamanhoPadrao) {}

        private int Hash(string chave)
        {
            int tot = 0;
            for (int i = 0; i < chave.Length; i++)
                tot += (int)chave[i];
            return tot % tabelaDeHash.Length;
        }

}

