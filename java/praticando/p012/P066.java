package praticando.p012;

// AJUSTANDO CASO SEQUÊNCIAL

/**
 * Existe um caso de elementos com valores sequênciais no vetor dos passageiros
 * que está retornando um valor que não é o esperado.
 * 
 * Exemplo:
 * []
 * 
 * Para resolver este problema, será feito anteriormente uma verificação se existe valores contínuos por todo o vetor de passageiros.
 * Existindo alguma sequência de valores
 */

import java.util.Arrays;

public class P066 {
    public static int ultimoHorario(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(buses);
        Arrays.sort(passengers);

        int esquerda = 0;
        int direita = buses[buses.length - 1];
        int ultimaPossibilidadeChegada = direita;


        // BUSCA BINÁRIA
        while (esquerda <= direita) {
            int meio = esquerda + (direita - esquerda) / 2;

            if (podeEntrarPassageiro(buses, passengers, capacity, meio)) {
                ultimaPossibilidadeChegada = meio;
                esquerda = meio + 1;
            } else {
                direita = meio - 1;
            }
        }

        return ultimaPossibilidadeChegada;
    }

    static boolean podeEntrarPassageiro(int[] buses, int[] passengers, int capacity, int arrivalTime) {
        int passengerIndex = 0;

        for (int busTime : buses) {
            int passageirosEntraram = 0;
            while (passengerIndex < passengers.length && passengers[passengerIndex] <= busTime && passageirosEntraram < capacity) {
                if (passengers[passengerIndex] <= arrivalTime) {
                    passageirosEntraram++;
                }
                passengerIndex++;
            }
        }

        return passengerIndex == passengers.length;
    }

    public static void main(String[] args) {
        int[] buses = {10, 20};
        int[] passengers = {2, 4, 17, 19};
        int capacity = 2;
        System.out.println(ultimoHorario(buses, passengers, capacity));
    }
}