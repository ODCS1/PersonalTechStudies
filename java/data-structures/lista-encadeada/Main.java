public class Main {
    public static void main(String[] args) {
        ListaEncadeada<Integer> lista = new ListaEncadeada<>();

        lista.adicionar(1);
        lista.adicionar(2);
        lista.adicionar(3);

        // System.out.println("Tamanho: " + lista.getTamanho());
        // System.out.println(lista.toString());

        // System.out.println();

        // lista.limpaOtimizado2();

        // System.out.println("LIMPA OTIMIZADO: " + lista.toString());
        // System.out.println();

        // lista.adicionar(7);
        // lista.adicionar(6);

        // System.out.println("LISTA: " + lista.toString());
        // System.out.println();

        // lista.limpaSimples();
        // System.out.println("LIMPA SIMPLES: " + lista.toString());
        // System.out.println();

        // lista.adicionar(9);
        // lista.adicionar(54);
        // lista.adicionar(754);

        // System.out.println();
        // System.out.println(lista.toString());

        // // BUSCA POR ELEMENTO
        // System.out.println("POSIÇÃO DO ELEMENTO 2: " + lista.buscaPorElemento(2));
        // System.out.println("POSIÇÃO DO ELEMENTO 2: " + lista.buscaPorElemento(9));
        // System.out.println();

        // // System.out.println(lista.buscaPorPosicaoWhile(0));
        // // BUSCA POR POSIÇÃO - WHILE
        // System.out.println("ELEMENTO NA POSIÇÃO 0(while): " + Integer.toString(lista.buscaPorPosicaoWhile(0)));
        // System.out.println("ELEMENTO NA POSIÇÃO 2(while): " + Integer.toString(lista.buscaPorPosicaoWhile(2)));
        // System.out.println();

        // // BUSCA POR POSIÇÃO - FOR
        // System.out.println("ELEMENTO NA POSIÇÃO 0(for): " + Integer.toString(lista.buscaPorPosicaoFor(0)));
        // System.out.println("ELEMENTO NA POSIÇÃO 2(for): " + Integer.toString(lista.buscaPorPosicaoFor(2)));

        // // INSERIR ELEMENTO NO INICIO
        // lista.inserirPorPosicao(0, 8);
        // lista.inserirNoInicio(15);
        // System.out.println(lista.toString());

        // // INSERIR ELEMENTO NO FIM
        // int tamanho = lista.getTamanho();
        // lista.inserirPorPosicao(tamanho, 50);
        // System.out.println(lista.toString());

        // // INSERIR ELEMENTO NO MEIO
        // lista.inserirPorPosicao(tamanho - 2, 346);
        // System.out.println(lista.toString());

        // System.out.println("TAMANHO: " + Integer.toString(lista.getTamanho()));

        // // REMOVE DO INICIO
        // System.out.println(lista.toString());
        // int elemento = lista.removeDoInicio();
        // System.out.println("ELEMENTO REMOVIDO: " + elemento);
        // System.out.println(lista.toString());

        // lista.removeDoInicio();
        // System.out.println(lista.toString());
        // lista.removeDoInicio();
        // System.out.println(lista.toString());

        // try {

        //     lista.removeDoInicio();
        // } catch (Exception e) {
        //     // TODO: handle exception
        //     System.out.println(e);
        // }

        // // REMOVE DO FIM
        // System.out.println(lista.toString());
        // System.out.println("ELEMENTO REMOVIDO: " + lista.removeDoFim());
        // System.out.println(lista.toString());

        // lista.removeDoFim();
        // System.out.println(lista.toString());
        // lista.removeDoFim();
        // System.out.println(lista.toString());

        // try {
        //     lista.removeDoFim();
        // } catch (Exception e) {
        //     // TODO: handle exception
        //     System.out.println(e);
        // }

        // REMOVE PELA POSIÇÃO
        // System.out.println(lista.toString());
        // int elemento = lista.removePorPosicao(2);
        // System.out.println("ELEMENTO REMOVIDO: " + Integer.toString(elemento));
        // System.out.println(lista.toString());

        // lista.removePorPosicao(1);
        // System.out.println(lista.toString());

        // lista.removePorPosicao(0);
        // System.out.println(lista.toString());

        // try {
        //     lista.removePorPosicao(0);
        // } catch (Exception e) {
        //     // TODO: handle exception
        //     System.out.println(e);
        // }
    }
}
