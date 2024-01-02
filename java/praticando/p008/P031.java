package praticando.p008;

public class P031 {
    public static void main(String[] args) {
        // IGUALDADE
        String resposta = "Sim!";

        boolean resultado = resposta.equals("sim!");
        System.out.println(resultado);
        // false

        boolean resultado2 = resposta.equalsIgnoreCase("sim!");
        System.out.println(resultado2);
        // true

        // TAMANHO
        int tamanho = resposta.length();
        System.out.println(tamanho);
        // 4

        // RETORNA UM DADO CHAR
        char retorno = resposta.charAt(0);
        System.out.println(retorno);
        // S

        // RETORNA A POSIÇÃO DO CHAR
        int posicao = resposta.indexOf("S");
        System.out.println(posicao);
        // 0

        // VERIFICAR SE A STRING ESTÁ VAZIA
        boolean vazio = resposta.isEmpty();
        System.out.println(vazio);
        // false

        // TUDO MAIÚSCULA
        String maiuscula = resposta.toUpperCase();
        System.out.println(maiuscula);
        // SIM!

        // TUDO MINÚSCULA
        String minuscula = resposta.toLowerCase();
        System.out.println(minuscula);
        // sim!

        // REMOVER ESPAÇO
        resposta = "  Sim!  ";
        String semEspaco = resposta.trim();
        System.out.println(semEspaco);
        // Sim!

        // SUBSTITUIR
        resposta = "Sim!";
        String troca = resposta.replace('S', 'N');
        System.out.println(troca);
        // Nim!

        // SUBSTRING ATÉ O FINAL
        String substring = resposta.substring(1);
        System.out.println(substring);
        // im!

        // SUBSTRING ATÉ O INFORMADO
        String substring2 = resposta.substring(1, 3);
        System.out.println(substring2);
        // im

        // COMEÇA COM?
        String str = "Olá, mundo!";
        boolean comecaCom = str.startsWith("Olá");
        System.out.println(comecaCom);
        // true

        // TERMINA COM?
        boolean terminaCom = str.endsWith("sistema!");
        System.out.println(terminaCom);
        // false

    }
}
