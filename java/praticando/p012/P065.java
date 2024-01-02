package praticando.p012;

import java.util.Arrays;

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
        int[] buses = {5, 8, 10};
        int[] passengers = {2, 4, 6, 8, 10};
        int capacity = 2;
        System.out.println(ultimoHorario(buses, passengers, capacity));
    }
}