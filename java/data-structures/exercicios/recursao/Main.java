public class Main
{
    public static boolean isNegativo (int a,int d)
    {
		if (a==0) return true;
		if (d==0) return false;
		return isNegativo(++a,--d);
	}
	
    public static boolean isNegativo (int x)
    {
        if (x==0) return false;
        return isNegativo(x,x);
    }

    public static int soma (int x,int y)
    {
		if (y==0) return x;
		if (isNegativo(y)) return soma(--x,++y);
		return soma(++x,--y);
	}
	
    public static int subtracao (int x,int y)
    {
		if (y==0) return x;
		if (isNegativo(y)) return subtracao(++x,++y);
		return subtracao(--x,--y);
	}

    public static void main (String[] args)
    {
        System.out.printf ("5-0 dá %d\n", subtracao(5,0));
        System.out.printf ("0-5 dá %d\n", subtracao(0,5));
        System.out.printf ("-3-7 dá %d\n", subtracao(-3,7));
        System.out.printf ("-3-(-5) dá %d\n", subtracao(-3,-5));
        System.out.printf ("3-(-5) dá %d\n", subtracao(3,-5));
        System.out.printf ("3-5 dá %d\n", subtracao(3,5));
        System.out.printf ("0-0 dá %d\n", subtracao(0,0));

        /* TESTES DO EXERCÍCIO 2:
 
        System.out.printf ("5+0 dá %d\n", soma(5,0));
        System.out.printf ("0+5 dá %d\n", soma(0,5));
        System.out.printf ("-3+7 dá %d\n", soma(-3,7));
        System.out.printf ("-3+(-5) dá %d\n", soma(-3,-5));
        System.out.printf ("3+(-5) dá %d\n", soma(3,-5));
        System.out.printf ("3+5 dá %d\n", soma(3,5));
        System.out.printf ("0+0 dá %d\n", soma(0,0));
        */
		/* TESTES DO EXERCÍCIO 1:
		
        if (isNegativo(-5))
            System.out.println ("-5 É negativo!");
        else
            System.out.println ("-5 NÃO é negativo!");
            
        if (isNegativo(0))
            System.out.println ("0 É negativo!");
        else
            System.out.println ("0 NÃO é negativo!");

        if (isNegativo(5))
            System.out.println ("5 É negativo!");
        else
            System.out.println ("5 NÃO é negativo!");
        */
        
    }
}
