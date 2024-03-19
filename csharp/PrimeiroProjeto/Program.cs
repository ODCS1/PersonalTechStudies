using PrimeiroProjeto;

// See https://aka.ms/new-console-template for more information


Lampada lamp = new Lampada();

lamp.mostraEstado();

Data hoje = new Data();

// USO DE MÉTODOS PARA TER ACESSO AO ATRIBUTO PRIVATE
hoje.setDia(6);
Console.WriteLine(hoje.getDia());


// USO DE PROPRIEDADE
hoje.Mes = 3; // SET É ACIONADO
Console.WriteLine(hoje.Mes); // GET É ACIONADO
Console.WriteLine(hoje.ToString());

Console.ReadLine();
