package praticando.p013;

import java.io.*;
import java.net.*;

// AQUI É O PROGRAMA REATIVO QUE INICIA O SERVIDOR DE FATO NO MÉTODO MAIN

// ACEITANDO A CONEXÃO DE NOVOS CLIENTE AQUI

// SERVE BASICAMENTENTE PARA INICIALIZAÇÃO E GERENCIAMENTO DE NOVAS CONEXÕES

public class Servidor {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(5000);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                ConexaoReativa conexao = new ConexaoReativa(clientSocket);
                conexao.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

