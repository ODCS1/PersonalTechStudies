public class ListaEncadeada<T> {
    private No<T> inicio;
    private No<T> ultimo;
    private int tamanho;
    private final int NAO_ENCONTRADO = -1;

    public void adicionar(T elemento) {
        No<T> novo = new No<T>(elemento);
        if (tamanho == 0) {
            inicio = novo;    
        } else {
            this.ultimo.setProximo(novo);
        }
        
        this.ultimo = novo;
        this.tamanho++;
    }

    public int getTamanho() {
        return this.tamanho;
    }
    
    public void limpaSimples() {
        this.inicio = null;
        this.ultimo = null;
        this.tamanho = 0;
    }


    // NÃO TÃO BOM, MAS FUNCIONA.
    public void limpaOtimizado1() {
        if (this.tamanho == 0)
            return;

        for (int i = 0; i < this.tamanho - 1; i++) {

            No<T> atual = this.inicio.getProximo();
            this.inicio.setElemento(null);
            this.inicio.setProximo(null);

            this.inicio = atual;
        }

        this.inicio.setElemento(null);
        this.tamanho = 0;
    }
    
    // MELHOR
    public void limpaOtimizado2() {
        No<T> atual = this.inicio.getProximo();

        while (atual != null) {
            No<T> proximo = atual.getProximo();
            atual.setElemento(null);
            atual.setProximo(null);

            atual = proximo;
        }

        this.inicio = null;
        this.ultimo = null;
        this.tamanho = 0;
    }
    
    private No<T> buscaNoPorPosicaoWhile(int pos) {
        if (pos < 0 || pos > this.tamanho) {
            throw new IllegalArgumentException("NÃO EXISTE ESSA POSIÇÃO!!!");
        }

        int c = 0;
        No<T> atual = inicio;
        while (atual.getProximo() != null) {
            if (c == pos)
                return atual;

            atual = atual.getProximo();
        }

        return atual;
    }
    
    private No<T> buscaNoPorPosicaoFor(int pos) {
        if (pos < 0 || pos > this.tamanho){
            throw new IllegalArgumentException("NÃO EXISTE ESSA POSIÇÃO!!!");
        }


        No<T> atual = inicio;

        for (int i = 0; i < pos; i++){
            atual = atual.getProximo();
        }

        return atual;
    }

    public T buscaPorPosicaoWhile(int pos){
        return buscaNoPorPosicaoWhile(pos).getElemento();
    }

    public T buscaPorPosicaoFor(int pos){
        return buscaNoPorPosicaoFor(pos).getElemento();
    }

    public int buscaPorElemento(T elemento) {
        No<T> noAtual = this.inicio;

        for (int i = 0; i < this.tamanho; i++) {
            if (noAtual.getElemento().equals(elemento)) {
                return i;
            }

            noAtual = noAtual.getProximo();
        }

        return NAO_ENCONTRADO;
    }
    

    public void inserirNoInicio(T elemento){
        // if (pos != 0) {
        //     throw new IllegalArgumentException("POSIÇÃO NÃO EXISTE!!!");
        // }

        // 2 SITUAÇÕES

        No<T> novoNo = new No<T>(elemento);

        // 1º - TAMANHO = 0
        if (this.tamanho == 0) {
            this.inicio = novoNo;
            this.ultimo = novoNo;
        }
        // 2º - TAMANHO > 0
        else {
            novoNo.setProximo(inicio);
            this.inicio = novoNo;
        }

        tamanho++;
    }

    public void inserirPorPosicao(int pos, T elemento) {
        if (pos < 0 || pos > tamanho) {
            throw new IllegalArgumentException("POSIÇÃO NÃO EXISTE!!!");
        }

        // 3 CASOS

        // 1º CASO - INSERIR NA POSIÇÃO 0
        if (pos == 0) {
            inserirNoInicio(elemento);
        }
        // 2º CASO - INSERIR NO FINAL
        else if (pos == this.tamanho) {
            adicionar(elemento);
        }
        // 3º CASO - INSERIR NO MEIO
        else {
            No<T> noPos = buscaNoPorPosicaoFor(pos);
            No<T> noAnterior = buscaNoPorPosicaoFor(pos - 1);

            No<T> noParaInserir = new No<T>(elemento);

            noParaInserir.setProximo(noPos);
            noAnterior.setProximo(noParaInserir);

            this.tamanho++;
        }
    }
    
    public T removeDoInicio() {
        if (this.tamanho == 0)
            throw new RuntimeException("NÃO EXISTE ELEMENTO PARA REMOVER!!!");

        T elementoRemovido = inicio.getElemento();
        No<T> novoInicio = inicio.getProximo();
        inicio.setElemento(null);
        inicio.setProximo(null);

        inicio = novoInicio;
        this.tamanho--;

        if (this.tamanho == 0)
            this.ultimo = null;

        return elementoRemovido;
    }

    public T removeDoFim() {
        if (this.tamanho == 0)
            throw new RuntimeException("NÃO EXISTE ELEMENTO PARA REMOVER!!!");

        T elementoRemovido = this.ultimo.getElemento();

        if (this.tamanho == 1) {
            this.inicio = null;
            this.ultimo = null;
            this.tamanho = 0;
            return elementoRemovido;
        }

        No<T> anterior = buscaNoPorPosicaoFor(this.tamanho - 2);
        anterior.setProximo(null);
        this.tamanho--;

        return elementoRemovido;
    }
    
    public T removePorPosicao(int pos) {
        if (this.tamanho == 0)
            throw new RuntimeException("SEM ELEMENTOS PARA REMOVER!!!");

        if (pos < 0 || pos > this.tamanho - 1)
            throw new IllegalArgumentException("A POSIÇÃO NÃO EXISTE!!!");
        
        if (this.tamanho == 1 || pos == this.tamanho - 1)
            return removeDoFim();
        else if (pos == 0)
            return removeDoInicio();


        No<T> noAnterior = buscaNoPorPosicaoWhile(pos - 1);
        No<T> noRemover = buscaNoPorPosicaoFor(pos);
        No<T> noPosterior = buscaNoPorPosicaoFor(pos + 1);

        T elementoRetorno = noRemover.getElemento();
        noRemover.setElemento(null);
        noRemover.setProximo(null);

        noAnterior.setProximo(noPosterior);
        this.tamanho--;

        return elementoRetorno;
    }


    // @Override
    // public String toString() {
    //     return "ListaEncadeada [inicio=" + inicio + "]";
    // }
    
    @Override
    public String toString() {
        if (this.tamanho == 0) return "[]";


        String saida = "[";
        No<T> atual = inicio;

        saida +=  atual.toString();

        while (atual.getProximo() != null) {
            atual = atual.getProximo();
            saida += ", " + atual.toString();
        }

        return saida + "]";
    }
}
