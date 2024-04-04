using System;
using System.Collections.Generic;

public class FilaVetor<Tipo> : IQueue<Tipo>
{
  public const int MAXIMO = 500; // tamanho default do vetor F

  int posicoes; // tamanho dado pela aplicação

  Tipo[] F; // vetor de objetos genéricos, com tamanho genérico,
            // usado como área de armazenamento

  int inicio = 0, // índice do início da fila
      fim = 0;    // índice do fim da fila

  public FilaVetor() : this(MAXIMO) // construtor que utiliza o default MAXIMO
  {                                 // chama o método construtor com parâmetro
  }                                 // utilizando o polimorfismo do construtor

  public FilaVetor(int posic) // construtor sobrecarregado
  {
    posicoes = posic;       // armazena o tamanho físico do vetor
    F = new Tipo[posicoes]; // F é um vetor de Tipo; cria um
  }                         // vetor F com o tamanho indicado

  public int Tamanho => (posicoes - inicio + fim) % posicoes;

  public bool EstaVazia => inicio == fim;

  public void Enfileirar(Tipo elemento)
  {
    if (Tamanho == posicoes - 1)
       throw new FilaCheiaException("Fila cheia (overflow)");

    // aqui, vetor ainda não está cheio, podemos enfileirar
    F[fim] = elemento;  // inclui elemento na primeira posição livre
    fim = (fim + 1) % posicoes; // calcula próxima posição livre
  }

  public Tipo OFim()
  {
    if (EstaVazia)
      throw new FilaVaziaException("Fila vazia!");

    Tipo ultimo;
    if (fim == 0)
      ultimo = F[posicoes - 1]; // devolve o objeto do final da fila
    else                        // sem retirá-lo da fila
      ultimo = F[fim - 1];

    return ultimo;
  }

  public Tipo OInicio()
  {
    if (EstaVazia)
      throw new FilaVaziaException("Esvaziamento (underflow) da fila");

    Tipo primeiro = F[inicio]; // devolve o objeto do início da fila
    return primeiro;           // sem retirá-lo da fila
  }

  public Tipo Retirar()
  {
    if (EstaVazia)
      throw 
  new FilaVaziaException("Esvaziamento da fila (underflow)");

    Tipo primeiro = F[inicio];  // copia o elemento inicial da fila
    F[inicio] = default(Tipo); // libera memória
    inicio = (inicio + 1) % posicoes; // calcula novo inicio da fila
    return primeiro; // devolve elemento inicial
  }

  public List<Tipo> Conteudo()
  {
    List<Tipo> resultado = new List<Tipo>();
    FilaVetor<Tipo> filaAuxiliar =
                      new FilaVetor<Tipo>(posicoes);

    while (!this.EstaVazia)   // fila original não esvaziou
    {
      var primeiro = this.Retirar();
      resultado.Add(primeiro);
      filaAuxiliar.Enfileirar(primeiro);  // enfileira cópias
    }

    while (!filaAuxiliar.EstaVazia)   // fila auxiliar não esvaziou
          this.Enfileirar(filaAuxiliar.Retirar());

    return resultado;
  }
}

