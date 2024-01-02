package praticando.p008;

public class P030 {
    public static void main(String[] args) {
        while (true) {
            for (int i = 1; i < 6; i++) {
                System.out.println("AA");
                if (i == 2) {
                    continue;
                }
                for (int j = 1; j < 4; j++) { 
                    if (j == 6) {
                        System.out.print("....");
                        break;
                    } else if (j < 4 ^ !(i > 5)) {
                        System.out.println("Continue...");
                        continue;
                    } else if (j == 2) {
                        System.out.println("");
                    }
                    System.out.print("AB" + j + ' ');
                }
                if (i == 4) {
                    break;
                }
                
            }
            break;
        }
    }
}
