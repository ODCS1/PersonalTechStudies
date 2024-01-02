package praticando.p004;
import java.awt.Dimension;
import java.awt.Toolkit;

public class GetResolution {
    public static void main(String[] args) {
        Toolkit t = Toolkit.getDefaultToolkit();
        Dimension dimensions = t.getScreenSize();
        int width = (int) dimensions.getWidth();
        int height = (int) dimensions.getHeight();
        System.out.println(String.format("Resolução da tela: %s x %s.", width, height));
    }
}

