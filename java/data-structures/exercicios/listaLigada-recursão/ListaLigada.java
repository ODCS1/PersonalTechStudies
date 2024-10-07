import org.w3c.dom.Node;

public class ListaLigada<T> {
    No<T> inicio;
    No<T> ultimo;

    public ListaLigada() {}
    
    

    public int quantidadeDeNo(No<T> no) {
        if (no == null) {
            return 0;
        }

        return 1 + quantidadeDeNo(no.getProximo());
    }
    
    public Boolean buscaPosicaoElemento(No<T> no, T elemento) {
        if (no == null) { return false; }
        

        if (no.getElemento().equals(elemento)) { return true; }

        
        return buscaPosicaoElemento(no.getProximo(), no.getProximo().getElemento());
    }
    

    public No<T> reverter(No<T> no) {
        if (no == null || no.getProximo() == null) {
            return no;
        }
        No novoNo = reverter(no.getProximo());
        no.setProximo().setProximo() = no;
        no.setProximo() = null;
        return novoNo;
    }

}
