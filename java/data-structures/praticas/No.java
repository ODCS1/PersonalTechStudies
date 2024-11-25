public class No<X> {
    private No<X> esquerdaNo;
    private X info;
    private No<X> direiNo;

    public No(No<X> e, X i, No<X> d) {
        this.esquerdaNo = e;
        this.info = i;
        this.direiNo = d;
    }

    public No(No<X> e, X i) {
        this.esquerdaNo = e;
        this.info = i;
        this.direiNo = null;
    }

    public No(X i, No<X> d) {
        this.esquerdaNo = null;
        this.info = i;
        this.direiNo = d;
    }

    public No(X i) {
        this.esquerdaNo = null;
        this.info = i;
        this.direiNo = null;
    }

    public No<X> getEsq ()
    {
        return this.esquerdaNo;
    }
    
    public X getInfo ()
    {
        return this.info;
    }
    
    public No<X> getDir ()
    {
        return this.direiNo;
    }
    
    public void setEsq (No<X> e)
    {
        this.esquerdaNo=e;
    }
    
    public void setInfo (X i)
    {
        this.info=i;
    }
    
    public void setDir (No<X> d)
    {
        this.direiNo=d;
    }

}