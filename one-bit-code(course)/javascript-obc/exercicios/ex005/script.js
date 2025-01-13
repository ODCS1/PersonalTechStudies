/*  Escreva um programa que permita inserir o nome e o poder de ataque de um personagem e se ele possui um escudo, e então calcule a quantidade de dano causado baseado nas seguintes regras:

  - Se o poder de ataque for maior do que a defesa e o defensor não possuir um escudo, o dano causado será igual a diferença entre o ataque e a defesa.
  
  - Se o poder de ataque for maior do que a defesa e o defensor possuir um escudo, o dano causado será igual a metade da diferença entre o ataque e a defesa.

  - Se o poder de ataque for menor ou igual a defesa, o dano causado será 0.

Por fim, o programa deve subtrair a quantidade de dano da quantidade de pontos de vida do personagem defensor e exibir na tela a quantidade de dano e as informações atualizadas de ambos os personagens.
*/

let atacante = prompt("Nome do personagem atacante ");
let poder_atq = Number(prompt("Poder de ataque: "));

let defensor = prompt("Nome do personagem defensor: ");
let poder_def = Number(prompt("Poder de defesa: "));
let pontos_vida = Number(prompt("Pontos de vida: "));
const escudo = prompt("Tem escudo[s/n]: ").toLowerCase();


dano = 0;
if (poder_atq > poder_def && escudo == "n") {
  dano = poder_atq - poder_def;
} else if ((poder_atq > poder_def) & (escudo == "s")) {
  dano = (poder_atq - poder_def) / 2;
} else {
  dano = 0;
}

pontos_vida -= dano;

alert(`${atacante} causou ${dano} pontos de dano em ${defensor}.`);
alert(`
  ${atacante} \nPoder de ataque: ${poder_atq} \n\n
  ${defensor} \nPoder de defesa: ${poder_def} \nPossuí escudo: ${escudo} \nPontos de vida: ${pontos_vida}.
`);



// let nome_atacante = window.prompt('Nome do atacante: ')
// let poder_ataque = Number(prompt('Poder de ataque: '))


// let nome_defensor = prompt('Nome do defensor: ')
// let defesa = Number('Defesa: ')
// let pontos_vida1 = Number('Pontos de vida:')
// let escudo2 = prompt('Tem escudo[s/n]: ').toLowerCase()

// dano = 0
// if (poder_ataque > defesa && escudo2 == 'n'){
//   dano = poder_ataque - defesa
// }else if (poder_ataque > defesa && escudo2 == 's'){
//   dano = poder_ataque - defesa / 2
// }else if (poder_ataque < defesa){
//   dano = 0
// }

// pontos_vida1 -= dano
// window.alert(`\t${nome_atacante} \nPoder de Ataque: ${poder_ataque} \n\t${nome_defensor} \nPoder de defesa: ${defesa} \nTem escudo: ${escudo} \nPontos de vida inicial: ${pontos_vida1 + dano} \nPontos de vida após ataque: ${pontos_vida1}`)