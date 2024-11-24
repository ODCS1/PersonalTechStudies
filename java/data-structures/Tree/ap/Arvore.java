package ap;

public class Arvore <X extends Comparable<X>> implements Cloneable
{
	private class No implements Cloneable
	{
		private No esq;
	    private X  info;
	    private No dir;
	    
	    public No (No e, X i, No d)
	    {
			this.esq =e;
	        this.info=i;
	        this.dir =d;
	    }
	    
	    public No (No e, X i)
	    {
			this.esq =e;
	        this.info=i;
	        this.dir =null;
	    }
	    
	    public No (X i, No d)
	    {
			this.esq =null;
	        this.info=i;
	        this.dir =d;
	    }
	    
	    public No (X i)
	    {
			this.esq =null;
	        this.info=i;
	        this.dir =null;
	    }
	    
	    public No getEsq ()
	    {
	        return this.esq;
	    }
	    
	    public X getInfo ()
	    {
	        return this.info;
	    }
	    
	    public No getDir ()
	    {
	        return this.dir;
	    }
	    
	    public void setEsq (No e)
	    {
	        this.esq=e;
	    }
	    
	    public void setInfo (X i)
	    {
	        this.info=i;
	    }
	    
	    public void setDir (No d)
	    {
	        this.dir=d;
	    }
	}
	
	private No raiz;
	
	public Arvore ()
	{
		this.raiz = null;
	}
	
	public void guarde (X i) throws Exception
	{
		if (i==null) throw new Exception ("Informação ausente");
		
		X copia;
		if (i instanceof Cloneable)
		    copia = new Clonador<X>().clone(i);
		else
		    copia = i;
		
		if (this.raiz==null)
		{
			this.raiz = new No (copia);
			return;
		}
		
		No atual=this.raiz;
		for(;;) // for ever
		{
			int comparacao = i.compareTo(atual.getInfo());
			
			if (comparacao==0) throw new Exception ("Informacao repetida");
			
			if (comparacao<0)
			{
			    if (atual.getEsq()==null)
			    {
			        atual.setEsq(new No (copia));
			        return;
				}
				else
				    atual=atual.getEsq();
			}
			else
			{ 
			    if (atual.getDir()==null)
			    {
			        atual.setDir(new No (copia));
			        return;
				}
				else
				    atual=atual.getDir();
			}
		}
	}
	
    public boolean tem (X i) throws Exception
    {
		// procurar i na arvore; achou retorna true;
		// nao achou, retorna false
	}
}
