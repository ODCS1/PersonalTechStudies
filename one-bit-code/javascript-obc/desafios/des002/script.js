/** CALCULADORA GEOMÉTRICA
 * 
 *  Escreva um programa em javascript para calcular a área de diferentes
 * formas geométricas. O programa deve iniciar com um menu contendo as
 * diferentes opções de cálculas. As opções devem ser:
 * 
 * - Área do triângulo: base * altura / 2
 * - Área do retângulo: base * altura
 * - Área do quadrado: lado^2
 * - Área do trapézio: (base maior + base menor) * altura / 2
 * - Área do círculo: pi * raio^2 (considere pi = 3.14)
 * 
 * Você deve escrever o programa usando funções sempre que possível para separar
 * os procedimentos. O programa também, deve ter uma opção de "Sair" e enquanto ela não for escolhida deverá voltar ao menu.
 */

function menu() {
    do {
        let num = prompt("Escolha uma opção Abaixo \n[1] Área do Triângulo \n[2] Área do Retângulo \n[3] Área do quadrado \n[4] Área do Trapézio \n[5] Área do círculo \n[6] SAIR")

        if (isNaN(num)) {
            alert("Por favor, insira um número válido.")
            continue
        } else if (1 > num || num > 6) {
            alert("Por favor, insira um número válido.")
            continue
        }else {
            num = Number(num)
            return num
        }
    } while (true)
}

function verificaNum (n) {
    while (true) {
        if (isNaN(n)) {
            alert("Por favor, insira um número válido.")
            return false
        } else if (n <= 0) {
            alert("Por favor, insira um número válido.")
            return false
        } else {
            return true
        }
    }
}

function calculaBase () {
    let base
    while (true) {
        base = prompt("Digite o valor da base: ")
        let ehnum = verificaNum(base)
        
        if (ehnum) {
            base = Number(base)
            return base
        } else{
            continue
        }
    }
}

function calculaAltura () {
    let altura
    while (true) {
        altura = prompt("Digite o valor da altura: ")
        let ehnum = verificaNum(altura)
        
        if (ehnum) {
            altura = Number(altura)
            return altura
        } else{
            continue
        }
    }
}

function calculaBaseMaior () {
    let baseMaior
    while (true) {
        baseMaior = prompt("Digite o valor da base maior: ")
        let ehnum = verificaNum(baseMaior)
        
        if (ehnum) {
            baseMaior = Number(baseMaior)
            return baseMaior
        } else{
            continue
        }
    }
}

function calculaBaseMenor () {
    let baseMenor
    while (true) {
        baseMenor = prompt("Digite o valor da base menor: ")
        let ehnum = verificaNum(baseMenor)
        
        if (ehnum) {
            baseMenor = Number(baseMenor)
            return baseMenor
        } else{
            continue
        }
    }
}

function calculaRaio () {
    let raio
    while (true) {
        raio = prompt("Digite o valor do raio: ")
        let ehnum = verificaNum(raio)
        
        if (ehnum) {
            raio = Number(raio)
            return raio
        } else{
            continue
        }
    }
}

function realizaCalculo (op) {
    let base;
    let altura;
    let baseMaior;
    let baseMenor;
    let raio;
    switch (op) {
        case 1, 2:  
            base = calculaBase()
            altura = calculaAltura()

            if (op === 1){
                return (base * altura) / 2
            } else {
                return (base * altura)
            }
        case 3:
            base = calculaBase()
            return base * base
        
        case 4:
            baseMaior = calculaBaseMaior()
            baseMenor = calculaBaseMenor()
            altura = calculaAltura()
            return (baseMaior + baseMenor) * altura / 2
        
        case 5:
            raio = calculaRaio()
            return 3.14 * (raio**2)
    }
}

function main() {
    do {
        let opcao = menu()
        alert("Você escolheu a opção " + opcao)
        if (opcao != 6){
            alert(`Resultado: ${realizaCalculo(opcao)}`)
        }
    } while(opcao != 6)
    
    alert('SAINDO...')
}

main()
