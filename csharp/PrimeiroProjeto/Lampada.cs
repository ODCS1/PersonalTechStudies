using System;
namespace PrimeiroProjeto
{
	public class Lampada
	{
		private bool ligada;
		public Lampada()
		{
		}

		public void ligar()
		{
			this.ligada = true;
		}

        public void desligar()
        {
            this.ligada = false;
        }

        public void mostraEstado()
		{
			if (ligada)
			{
                Console.WriteLine("Está ligado!!!");
            }else
			{
				Console.WriteLine("Está desligado!!!");
			}
			
		}
	}
}

