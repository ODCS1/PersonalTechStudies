using System;
using System.Collections.Generic;

public interface IQueue<Tipo>
{
  void Enfileirar(Tipo elemento); // inclui novo elemento ao final da fila
  Tipo Retirar();    // remove e retorna o 1o elemento da fila

  Tipo OInicio();    // devolve objeto do início da fila
                     // sem retirá-lo da fila

  Tipo OFim();       // devolve objeto do fim da fila
                     // sem retirá-lo da fila

  int Tamanho { get; } // devolve número de elementos da fila

  bool EstaVazia { get; } // informa se a fila está vazia ou não

  List<Tipo> Conteudo(); // retorna o conteúdo da fila sem estragá-la
}

