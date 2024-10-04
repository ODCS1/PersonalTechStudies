public class No<T>{
    private T elemento;
    private No<T> proximo;

    public No(T elemento){
        if (elemento == null) throw new IlegalArgumentException("ELEMENTO NÃO PODE SER NULO!!!");

        this.elemento = elemento;
    }

    public No(T elemento, No<T> proximo){
        if (elemento = null) throw new IlegalArgumentException("ELEMENTO NÃO PODE SER NULO!!!");

        this.elemento = elemento;
        this.proximo = proximo;
    }

    public T getElemento() {
        return elemento;
    }

    public void setElemento(T elemento) {
        this.elemento = elemento;
    }

    public No<T> getProximo() {
        return proximo;
    }

    public void setProximo(No<T> proximo) {
        this.proximo = proximo;
    }

    @Override
    public String toString(){
        if (elemento != null)
            return elemento.toString();
        else
            return "null";
    }
}
