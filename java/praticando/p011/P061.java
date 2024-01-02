package praticando.p011;

// public class P061 {
//     public static void main(String[] args) {
        
//         int num;
//         if (true) {
//             // Escopo local
//             num = 10;
//             System.out.println("Local: " + num);
//         }

//         System.out.println("Global: " + num);
//     }
// }

// public class P061 {
//     static int num;
//     public static void main(String[] args) {
        
//         num = 2;
//         System.out.println("Local: " + num);

//         escopo();
//     }

//     static void escopo () {
//         System.out.println("Global: " + num);
//     }
// }

public class P061 {
    public static void main(String[] args) {
        
        int num = 2;
        System.out.println("Local (main): " + num);

        escopo(num);
        System.out.println("Local (main): " + num);
    }

    static void escopo (int num) {
        num += 2;
        System.out.println("Local (escopo): " + num);
    }
}


