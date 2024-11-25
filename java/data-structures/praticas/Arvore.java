public class Arvore<X extends Comparable<X>> implements Cloneable {
    private No<X> raiz;

    public Arvore(){
        this.raiz = null;
    }



    public void guarde(X i) throws Exception{
        if (i == null) throw new Exception("IFORMAÇÃO AUSENTE! ");

        X copia;
        if (i instanceof Cloneable){
            copia = new Clonador<X>().clone(i);
        }else {
            copia = i;
        }

        if (this.raiz == null){
            this.raiz = new No<X>(copia);
            return;
        }

        No<X> noAtual = this.raiz;
        for(;;){
            int comparacao = i.compareTo(copia);

            if (comparacao == 0) throw new Exception("INFIRMAÇÃO REPETIDA! ");

            if (comparacao < 0){
                if (noAtual.getEsq() == null){
                    noAtual.setEsq(new No<X>(copia);
                    return;
                }
                noAtual = noAtual.getEsq();
            }else {
                if (noAtual.getDir() == null){
                    noAtual.setDir(new No<X>(copia);
                    return;
                }
                noAtual = noAtual.getDir();
            }
            
        }
    }




    // public void guarde(X i) throws Exception{

    //     if (i == null) { throw new IllegalArgumentException("INFORMAÇÃO AUSENTE."); }

    //     X copia;
    //     if (i instanceof Cloneable){
    //         copia = new Clonador<X>().clone(i);
    //     }else{
    //         copia = i;
    //     }

    //     if (raiz == null){
    //         this.raiz = new No<X>(copia);
    //         return;
    //     }

    //     No<X> noAtual = this.raiz;
    //     for(;;){
    //         int comparacao = i.compareTo(noAtual.getInfo());

    //         if (comparacao == 0) { throw new Exception("INFORMAÇÃO REPETIDA"); }

    //         if (comparacao < 0) {
    //             if (noAtual.getEsq() == null){
    //                 noAtual.setEsq(new No<X>(copia));
    //                 return;
    //             }
                
    //             noAtual = noAtual.getEsq();
    //         }else {
    //             if (noAtual.getDir() == null){
    //                 noAtual.setDir(new No<X>(copia));
    //                 return;
    //             }

    //             noAtual = noAtual.getDir();
    //         }
    //     }
    // }

    public void emOrdem(){
        emOrdemRec(raiz);
    }

    private void emOrdemRec(No<X> noAtual){
        if (noAtual != null){
            emOrdemRec(noAtual.getEsq());
            System.out.print(noAtual.getInfo() + " ");
            emOrdemRec(noAtual.getDir());
        } 
    }

    public void preOrdem(){
        preOrdemRec(raiz);
    }

    private void preOrdemRec(No<X> noAtual){
        if (noAtual != null){
            System.out.print(noAtual.getInfo() + " ");
            preOrdemRec(noAtual.getEsq());
            preOrdemRec(noAtual.getDir());
        }
    }

    public void posOrdem(){
        posOrdemRec(raiz);
    }

    private void posOrdemRec(No<X> noAtual){
        if (noAtual != null){
            posOrdemRec(noAtual.getEsq());
            posOrdemRec(noAtual.getDir());
            System.out.print(noAtual.getInfo() + " ");
        } 
    }

    public boolean temSemOrdem(X i) throws Exception{
        if (i == null) throw new Exception("INFORMAÇÃO AUSENTE! ");

        return temSemOrdemRec(raiz, i);
    }

    public boolean temSemOrdemRec(No<X> noAtual, X i){
        if (noAtual == null) { return false; }

        if (noAtual.getInfo().equals(i)) { return true; }

        return temSemOrdemRec(noAtual.getEsq(), i) || temSemOrdemRec(noAtual.getDir(), i);
    }


    public boolean temComOrdem(X i) throws Exception{
        if (i == null) throw new Exception("INFORMAÇÃO AUSENTE! ");

        return temComOrdemRec(raiz, i);
    }

    public boolean temComOrdemRec(No<X> noAtual, X i){
        if (noAtual == null) return false;

        int comparacao = i.compareTo(noAtual.getInfo());

        if (comparacao == 0) return true;

        if (comparacao < 0) { return temComOrdemRec(noAtual.getEsq(), i); }

        return temComOrdemRec(noAtual.getDir(), i);
    }


    // REMOVA UM ELEMENTO
    public void remova(X i) throws Exception {
        this.raiz = removaRec(this.raiz, i);
    }
    
    private No<X> removaRec(No<X> atual, X i) throws Exception {
        if (atual == null) throw new Exception("Elemento não encontrado");
    
        int comparacao = i.compareTo(atual.getInfo());
    
        if (comparacao < 0) {
            atual.setEsq(removaRec(atual.getEsq(), i));
        } else if (comparacao > 0) {
            atual.setDir(removaRec(atual.getDir(), i));
        } else {
            if (atual.getEsq() == null) return atual.getDir();
            if (atual.getDir() == null) return atual.getEsq();
    
            X menor = encontrarMenor(atual.getDir());
            atual.setInfo(menor);
            atual.setDir(removaRec(atual.getDir(), menor));
        }
        return atual;
    }
    
    private X encontrarMenor(No<X> atual) {
        while (atual.getEsq() != null) {
            atual = atual.getEsq();
        }
        return atual.getInfo();
    }
    

    // ALTURA DA ÁRVORE
    public int altura() {
        return alturaRec(this.raiz);
    }
    
    private int alturaRec(No<X> atual) {
        if (atual == null) return -1;
    
        int alturaEsq = alturaRec(atual.getEsq());
        int alturaDir = alturaRec(atual.getDir());
    
        return 1 + Math.max(alturaEsq, alturaDir);
    }


    // ÁRVORE É BALANCEADA
    public boolean ehBalanceada() {
        return ehBalanceadaRec(this.raiz);
    }
    
    private boolean ehBalanceadaRec(No<X> atual) {
        if (atual == null) return true;
    
        int alturaEsq = alturaRec(atual.getEsq());
        int alturaDir = alturaRec(atual.getDir());
    
        return Math.abs(alturaEsq - alturaDir) <= 1 
            && ehBalanceadaRec(atual.getEsq()) 
            && ehBalanceadaRec(atual.getDir());
    }

    
    // TOTAL DE NÓS
    public int contarNos() {
        return contarNosRec(this.raiz);
    }
    
    private int contarNosRec(No<X> atual) {
        if (atual == null) return 0;
    
        return 1 + contarNosRec(atual.getEsq()) + contarNosRec(atual.getDir());
    }
    
    // ESPELHAR ÁRVORE
    public void espelhar() {
        espelharRec(this.raiz);
    }
    
    private void espelharRec(No<X> atual) {
        if (atual != null) {
            No<X> temp = atual.getEsq();
            atual.setEsq(atual.getDir());
            atual.setDir(temp);
    
            espelharRec(atual.getEsq());
            espelharRec(atual.getDir());
        }
    }
    

    // IGUAIS
    public boolean saoIguais(Arvore<X> outra) {
        return saoIguaisRec(this.raiz, outra.raiz);
    }
    
    private boolean saoIguaisRec(No<X> no1, No<X> no2) {
        if (no1 == null && no2 == null) return true;
        if (no1 == null || no2 == null) return false;
    
        return no1.getInfo().equals(no2.getInfo())
            && saoIguaisRec(no1.getEsq(), no2.getEsq())
            && saoIguaisRec(no1.getDir(), no2.getDir());
    }

    

}
