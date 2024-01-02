package praticando.p008;

public class P028 {
    public static void main(String[] args) {
        String num = "Asc";

        switch (num) {
            case "kve":
                System.out.print("O valor é 0.");
                break;
            case "kde":
                System.out.print("O valor é 1.");
                break;
            case "Asc":
                System.out.print("O valor é 2.");
                break;
            case "kv":
                System.out.print("O valor é 3.");
                break;
            default:
                System.out.print("Valor fora do intervalo!");
        }
    }
}
