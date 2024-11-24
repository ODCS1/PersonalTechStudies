package ap;

public class Main
{
	public static void main (String[] args)
	{
		try
		{
			ListaEncadeadaSimplesDesordenada<Integer> l1;
			ListaEncadeadaSimplesDesordenada<String>  l2;
			
			l1 = new ListaEncadeadaSimplesDesordenada<Integer> ();
				
			l1.guardeNoInicio(1);
			l1.guardeNoInicio(2);
			l1.guardeNoInicio(3);
			l1.guardeNoInicio(4);
			l1.guardeNoInicio(5);
		
			//System.out.println(l1.toString());
			System.out.println(l1);
		
			l1.remova(1);
		
			System.out.println(l1);
		
			System.out.println(l1.tem(2)); // true
			System.out.println(l1.tem(9)); // false
			
			ListaEncadeadaSimplesDesordenada<Data> l3 = new ListaEncadeadaSimplesDesordenada<Data> ();
			Data natal = new Data ((byte)25,(byte)12,(short)2024);
			l3.guardeNoInicio(natal);
			natal.setAno((short)2025);
			
			Data reveillon;
			Data passagemDeAno = new Data (reveillon);
			
			Data christmas = (Data)natal.clone();
			
		}
		catch(Exception ex)
		{
			System.err.println(ex.getMessage());
		}
	}
}
