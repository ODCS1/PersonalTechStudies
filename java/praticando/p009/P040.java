package praticando.p009;

public class P040 {
    public static void main(String[] args) {
        // Autoboxing: int para Integer
        int inteiroPrimitivo = 53;
        Integer wrappedInt = inteiroPrimitivo;

        // Unboxing: Integer para int
        Integer wrappedInt2 = 78;
        int inteiroPrimitivo2 = wrappedInt2;
        System.out.println(inteiroPrimitivo2);

        // Operações com os valores
        int soma = wrappedInt + wrappedInt2;

        // Exibindo o resultado
        System.out.println("Soma: " + soma);
    }
}
