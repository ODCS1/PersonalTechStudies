package praticando.p007;
import javax.swing.JOptionPane;

public class P021 {
    public static void main(String[] args) {
        int cateto1 = Integer.parseInt(JOptionPane.showInputDialog("Valor do cateto oposto"));
        int cateto2 = Integer.parseInt(JOptionPane.showInputDialog("Valor do cateto adjacente"));
        double hipotenusa = Math.sqrt((cateto1*cateto1) + (cateto2*cateto2));

        JOptionPane.showMessageDialog(null, "Hipotenusa: " + hipotenusa);
        // System.out.printf("Cateto 1: %d \nCateto 2: %d \nHipotenusa: %.2f", cateto1, cateto2, hipotenusa);
    }
}