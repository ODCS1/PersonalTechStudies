using API_WEB;

namespace API_WEB
{
    public static class RepositorioDeProduto
    {

        public static List<Produto>? Produtos { get; set; }

        public static void Adicionar(Produto prod)
        {
            if (Produtos == null)
            {
                Produtos = new List<Produto>();
            }
            Produtos.Add(prod);
        }

        public static Produto? PegarPorCodigo(string cod)
        {
            if (Produtos != null)
                return Produtos.FirstOrDefault(p => p.Codigo == cod);
            return null;
        }

        public static void Alterar(Produto prod) 
        {
            if (Produtos != null)
            {
                Produto proCadastrado = Produtos.FirstOrDefault(P => P.Codigo == prod.Codigo);
            }
        }

        public static void Remover(Produto prod)
        {
            if (Produtos != null)
            {
                Produtos.Remove(prod);
            }
        }
    }
}




