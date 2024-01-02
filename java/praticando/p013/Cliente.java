package praticando.p013;

import java.io.*;
import java.net.*;

// NESSE ARQUIVO É ONDE O CLIENTE VAI ESTABELECER A CONEXÃO COM O SERVIDOR

public class Cliente {
    public static void main(String[] args) {
        try {
            // CONFIGURANDO O SOCKET DE CONEXÃO COM O SERVIDOR
            Socket socket = new Socket("localhost", 8000);

            // AS ENTRADAS DE USUÁRIO SÃO FEITAS COM O BUFFEREDREADER
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            // MANDANDO ESSAS ENTRADAS PARA O O SERVIDOR USANDO O PRINTWRITER
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // ESSAS ENTRADAS DE COMUNICAÇÃO COM O SERVIDOR USAM PARA ENTRADAS O InputStream
            // E PARA SAÍDA OutPutStream


            // ESSES SOCKETS PERMITE ESSA COMUNICAÇÃO ENTRE OS PROCESSOS EM DIFERENTES MÁQUINAS POR EXEMPLO
            // NESSE CASO AQUI, ESSA COMUNICAÇÃO É NO MESMO COMPUTADOR, MAS PODERIA SER UM COMPUTADOR
            // QUALQUER SE COMUNICANDO COM O COMPUTADOR COM O SERVIDOR

            

            // SE O USUÁRIO DIGITAR SIM, IRÁ SER RETORNADO PARA ELE UM INTEIRO
            // CASO O USUÁRIO DIGITE ENCERRAR, SERÁ FECHADO A CONEXÃO
            String userInputLine;
            while ((userInputLine = userInput.readLine()) != null) {
                if (userInputLine.equalsIgnoreCase("SIM") || userInputLine.equalsIgnoreCase("FIM")) {
                    out.println(userInputLine);
                    if (userInputLine.equalsIgnoreCase("ENCERRAR")) {
                        socket.close();
                        break;
                    } else {
                        String serverResponse = in.readLine();
                        System.out.println("Valor recebido do servidor: " + serverResponse);
                    }
                } else {
                    System.out.println("Digite 'SIM' ou 'ENCERRAR'");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

