public class ListaLigada<T>{
    private No<T> primeiro;
    private No<T> ultimo;
    private int tamanho;

    public ListaLigada(){

    }

    private void verificaElementoNulo(T elemento){
        if (elemento == null) throw new IlegalArgumentException("VOCÊ PASSOU UM ELEMENTO NULO!!!");
    }

    public void adicionarNoFinal(T elemento){
        verificaElementoNulo(elemento);

        No<T> noAtual = new No<T>(elemento);

        if (this.tamanho == 0){
            this.primeiro = noAtual;
            
        }else{
            this.ultimo.setProximo(noAtual);
        }

        this.ultimo = noAtual;
    }

    public void adicionarNoInicio(T elemento){
        verificaElementoNulo(elemento);

        No<T> novoNo = No<T>(elemento);

        if (this.tamanho == 0){
            this.ultimo = novoNo;
        }else{
            novoNo.setProximo(this.primeiro);
        }

        this.primeiro = novoNo;
    }
}