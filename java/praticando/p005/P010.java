// Conversão de tipos no Java

package praticando.p005;

public class P010 {
    public static void main(String[] args) {
        int idade = 30;
        String valor = Integer.toString(idade);
        System.out.println(valor);

        int num = Integer.parseInt(valor);

        int num2 = 10;

        System.out.println(num + num2);

        // Com valores com ponto flutuante

        String valorFloat = "10.5";
        float numFloat = Float.parseFloat(valorFloat);

        System.out.println(numFloat + " e " + valorFloat);

        float num2Float = 12.3f;
        String valorNum2Float = Float.toString(num2Float);

        System.out.println(num2Float + " e " + valorNum2Float);
    }
}
