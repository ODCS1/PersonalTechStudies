//  Verificador de idade para condições de voto
 
 var idade = 16;

 if (idade < 16){
  console.log('Não pode votar')
 } else if (idade < 18 || idade > 70){
  console.log('Voto opcional')
 } else{
  console.log('Voto Obrigatório')
 }