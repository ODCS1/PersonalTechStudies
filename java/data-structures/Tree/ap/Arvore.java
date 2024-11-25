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

	public void emOrdem(){ emOrdem(this.raiz); }

	public void emOrdem(No atual) {
		if (atual != null) {
			emOrdem(atual.getEsq());
			System.out.println(atual.getInfo());
			emOrdem(atual.getDir());
		}
	}

	public void preOrdem(){ preOrdem(this.raiz); }

	public void preOrdem(No atual) {
		if (atual != null){
			System.out.println(atual.getInfo());
			preOrdem(atual.getEsq());
			preOrdem(atual.getDir());
		}
	}

	public void posOrdem() { preOrdem(this.raiz); }

	public void posOrdem(No atual) {
		if (atual != null) {
			posOrdem(atual.getEsq());
			posOrdem(atual.getEsq());
			System.out.println(atual.getInfo());
		}
	}
	


	public boolean temSemOrdem(X i) throws Exception {
		if (i == null) 
			throw new Exception("Informação ausente");
	
		return temSemOrdem(this.raiz, i);
	}
	
	private boolean temSemOrdem(No atual, X i) throws Exception {
		if (atual == null) 
			return false;
	
		// Verifica o nó atual
		if (atual.getInfo().equals(i)) 
			return true;
	
		// Continua a busca na esquerda e na direita
		return temSemOrdem(atual.getEsq(), i) || temSemOrdem(atual.getDir(), i);
	}
	
	public boolean temComOrdem(X i) throws Exception {
		if (i == null) 
			throw new Exception("Informação ausente");
	
		return temComOrdem(this.raiz, i);
	}
	
	private boolean temComOrdem(No atual, X i) throws Exception {
		if (atual == null) 
			return false;
	
		int comparacao = i.compareTo(atual.getInfo());
	
		// Se encontrou o elemento
		if (comparacao == 0) 
			return true;
	
		// Se o valor buscado é menor, vai para a esquerda
		if (comparacao < 0) 
			return temComOrdem(atual.getEsq(), i);
	
		// Se o valor buscado é maior, vai para a direita
		return temComOrdem(atual.getDir(), i);
	}
	
}
