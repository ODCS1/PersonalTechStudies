package praticando.p012;




















// import java.util.Arrays;

// public class P064 {

//     public static int getLastBusTime(int[] buses, int[] passengers, int capacity) {
//         Arrays.sort(buses); // Ordenar os horários de partida dos ônibus em ordem crescente
//         Arrays.sort(passengers); // Ordenar os horários de chegada dos passageiros em ordem crescente

//         int lastTime = 0;
//         int busIndex = 0;
//         int passengerIndex = 0;

//         int tamBus = buses.length;
//         int qtdMaxP = capacity * tamBus;
//         int tamPass = passengers.length;
//         int dife;

//         if (tamPass > qtdMaxP) {
//             dife = tamPass - qtdMaxP;
//             while (busIndex < buses.length && passengerIndex < passengers.length - dife) {
//                 if (passengers[passengerIndex] <= buses[busIndex] && Math.abs(busIndex - passengerIndex) < capacity) {
//                     // O passageiro pode pegar o ônibus atual
//                     passengerIndex++;
//                 } else {
//                     // O passageiro precisa esperar pelo próximo ônibus
//                     lastTime = buses[busIndex];
//                     busIndex++;
//                 }
//             }

//             // Se ainda houver passageiros não acomodados, escolha o horário de chegada mais recente
//             while (passengerIndex < passengers.length - dife) {
//                 lastTime = passengers[passengerIndex];
//                 passengerIndex++;
//             }

//             // Se ainda houver ônibus disponíveis, escolha o horário de partida mais recente
//             while (busIndex < buses.length) {
//                 lastTime = buses[busIndex];
//                 busIndex++;
//             }
            

//         }else if (tamPass == qtdMaxP) {
//             // dife = tamPass - qtdMaxP;
//             while (busIndex < buses.length && passengerIndex < passengers.length) {
//                 if (passengers[passengerIndex] <= buses[busIndex] && Math.abs(busIndex - passengerIndex) < capacity) {
//                     // O passageiro pode pegar o ônibus atual
//                     passengerIndex++;
//                 } else {
//                     // O passageiro precisa esperar pelo próximo ônibus
//                     lastTime = buses[busIndex];
//                     busIndex++;
//                 }
//             }

//             // Se ainda houver passageiros não acomodados, escolha o horário de chegada mais recente
//             while (passengerIndex < passengers.length) {
//                 lastTime = passengers[passengerIndex];
//                 passengerIndex++;
//             }

//             // Se ainda houver ônibus disponíveis, escolha o horário de partida mais recente
//             while (busIndex < buses.length) {
//                 lastTime = buses[busIndex];
//                 busIndex++;
//             }
            
//         }else if (tamPass < qtdMaxP) {
//             dife = qtdMaxP - tamPass;
//             while (busIndex < buses.length && passengerIndex < passengers.length - dife) {
//                 if (passengers[passengerIndex] <= buses[busIndex] && Math.abs(busIndex - passengerIndex) < capacity) {
//                     // O passageiro pode pegar o ônibus atual
//                     passengerIndex++;
//                 } else {
//                     // O passageiro precisa esperar pelo próximo ônibus
//                     lastTime = buses[busIndex];
//                     busIndex++;
//                 }
//             }

//             // Se ainda houver passageiros não acomodados, escolha o horário de chegada mais recente
//             while (passengerIndex < passengers.length - dife) {
//                 lastTime = passengers[passengerIndex];
//                 passengerIndex++;
//             }

//             // Se ainda houver ônibus disponíveis, escolha o horário de partida mais recente
//             while (busIndex < buses.length) {
//                 lastTime = buses[busIndex];
//                 busIndex++;
//             }
            
//         }
//         return lastTime;
//     }

//     public static void main(String[] args) {
//         int[] buses1 = {10, 20};
//         int[] passengers1 = {2, 17, 18, 19};
//         int capacity1 = 2;
//         System.out.println(getLastBusTime(buses1, passengers1, capacity1)); // Saída: 16

//         int[] buses2 = {20, 30, 10};
//         int[] passengers2 = {19, 13, 26, 4, 25, 11, 21};
//         int capacity2 = 2;
//         System.out.println(getLastBusTime(buses2, passengers2, capacity2)); // Saída: 20
//     }
// }
