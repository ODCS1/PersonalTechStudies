import "dart:io";
void main(){
    int numero = 10;
    print("Hello, World!\n");
    print("Número: " + numero.toString());

    var valor = true;
    dynamic nome = "Nome";
    print(nome.runtimeType.toString() + "\n");
    stdout.write(valor.runtimeType.toString() + " ");

    // JÁ SABE O VALOR DE INICIO
    const PI = 3.141592;

    // VAI RECEBER O VALOR DE UMA OPERAÇÃO
    final PI2 = 3.141592; 

    print(PI);
}