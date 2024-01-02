package praticando.p008;

public class P034 {
    public static void main(String[] args) {
        String[][] valores = {{"312", "432"}, {"23"}, {"7"}};
        for (int i = 0; i < valores.length; i++) {
            for (int j = 0; j < valores[i].length; j++) {
                System.out.println(valores[i][j]);
            }
        }
    }
}