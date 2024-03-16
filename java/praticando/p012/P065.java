package praticando.p012;

import java.util.Arrays;






// n ônibus
// m passageiros
// buses[] é uma lista para o horário dos ônibus
// passengers é uma lista para o horário que o passageiro chega no ponto de ônibus

// 1° ETAPA: ordenar os dois vetores
// 2° ETAPA: usar busca binária para entrar a posição válida
// 3° ETAPA: 




















public class P065 {
    public static int ultimoHorario(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(buses);
        Arrays.sort(passengers);

        int left = 0;
        int right = buses[buses.length - 1];
        int ultimaPossibilidadeChegada = right;


        // BUSCA BINÁRIA
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (podePassageiroEntrar(buses, passengers, capacity, mid)) {
                ultimaPossibilidadeChegada = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ultimaPossibilidadeChegada;
    }

    static boolean podePassageiroEntrar(int[] buses, int[] passengers, int capacity, int arrivalTime) {
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
        // int[] buses = {10, 20};
        // int[] passengers = {2, 17, 18, 19};

        int[] buses = {20,30,10};
        int[] passengers = {19,13,26,4,25,11,21};
        int capacity = 2;
        System.out.println(ultimoHorario(buses, passengers, capacity));
    }
}