package praticando.p013;

import java.io.*;
import java.net.*;

// AQUI É ONDE GERENCIA A CONEXÃO DE CLIENTE A CLIENTE

public class ConexaoReativa extends Thread {
    private Socket socket;
    private int numeroInteiro = 0;

    public ConexaoReativa(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        // AQUI DENTRO DO RUN, ESTÁ A LÓGICA PARA TRABALHAR COM AS MENSAGENS DOS CLIENTES
        // OU SEJA, LER, VERIFICAR E CONTROLAR O CICLO DE VIDA DESSA CONEXÃO.
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                if (inputLine.equalsIgnoreCase("SIM")) {
                    out.println(numeroInteiro);
                    numeroInteiro++;
                } else if (inputLine.equalsIgnoreCase("ENCERRAR")) {
                    socket.close();
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

