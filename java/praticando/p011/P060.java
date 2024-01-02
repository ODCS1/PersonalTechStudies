package praticando.p011;

public class P060 {
    public static void main(String[] args) {
        // Teclado tec1 = new Teclado();
        // tec1.espaco(' ');
        // tec1.shortcuts(String "ctrl", String "'");
        // tec1.escreverNum(5432);
        int[] vet = {4, 6, 2};

        System.out.println(sumVet(vet));
    }

    static int[] sumVet(int[] vet) {
        
        int len = vet.length * 2;
        
        int[] vet2 = new int[len];

        for (int c = vet.length; c < len; c++) {
            for (int i = 0; i < vet.length; i++) {
                vet2[i] = vet[i];
            }  
        }
        
        return vet2;
    }
}
