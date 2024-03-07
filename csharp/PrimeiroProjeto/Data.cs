using System;
namespace PrimeiroProjeto
{
	public class Uteis
	{
		public Uteis()
		{
		}

       public static string zerosAEsquerda(int numero)
       {
            if (numero > 9)
                return "" + numero;

            return "0" + numero;
        }

        public void teste()
        {
            Console.WriteLine("CORRETO!!!!");
        }
    }
}

