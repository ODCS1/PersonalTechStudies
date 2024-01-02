package praticando.p006;
import javax.swing.JOptionPane;

public class P019 {
    public static void main(String[] args) {
        // nome
        String nome = JOptionPane.showInputDialog("Digite o seu nome");
        JOptionPane.showMessageDialog(null, "Olá " + nome + "!");

        // idade
        int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a sua idade: "));
        JOptionPane.showMessageDialog(null, "Você tem " + idade + " anos.");

        // altura
        String alturaStr = JOptionPane.showInputDialog("Digite a sua altura em metros");
        double altura = alturaStr.indexOf(',') != -1 ? Double.parseDouble(alturaStr.replace(',', '.')) : Double.parseDouble(alturaStr);
        JOptionPane.showMessageDialog(null, "Você tem " + altura + " de altura.");
    }
}
