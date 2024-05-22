using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Horario
{
    public class Hora
    {
        public Hora()
        {
            int Horas = 0;
            int Minutos = 0;
            int Segundos = 0;
        }

        private int _horas;
        public int Horas
        {
            get => _horas;
            set
            {
                if (Math.Abs(_horas - value) >= 0)
                {
                    _horas = value;
                }
            }
        }

        private int _minutos;
        public int Minutos
        {
            get => _minutos;
            set
            {
                if (value >= 60)
                {
                    Horas += (int)value / 60;
                    _minutos = value % 60;
                }
                else
                {
                    _minutos = value;
                }
            }
        }




        private int _segundos;
        public int Segundos
        {
            get => _segundos;
            set
            {
                if (value >= 60)
                {
                    Minutos += (int)value / 60;
                    _segundos = value % 60;
                }
                else
                {
                    _segundos = value;
                }
            }
        }

        public void AddUmSegundo(int s)
        {
            Segundos += s;
        }

        public void AddUmMinuto(int s) {
            Minutos += s;
        }

        public void RemoverUmSegundo(int s)
        {
            int segudosTotais = (int) Horas/3600 + Minutos/60 + Segundos;
            if (segudosTotais - s >= 0)
            {
                Segundos -= s;
            }
            
        }

        public void RemoverUmMinuto(int s) 
        {
            int minutosTotais = (int) Horas / 60 + Minutos;
            if (minutosTotais - s >= 0)
            {
                Minutos -= s;
            }
        }

        
        public override String ToString()
        {
            return zerosAEsquerda(Horas) + ":" + zerosAEsquerda(Minutos) + ":" + zerosAEsquerda(Segundos);
        }

        public static string zerosAEsquerda(int numero)
        {
            if (numero > 9)
                return "" + numero;

            return "0" + numero;
        }

    }
}
