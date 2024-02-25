function verificar() {
  // conteúdo
  var content = document.querySelector("div#conteudo");
  var img = document.createElement("img");
  img.setAttribute("id", "foto");

  // Idade
  var anon = document.querySelector("input#iano").value;
  var anon = Number(anon);
  var agora = new Date();
  var anoa = agora.getFullYear();
  var idade = anoa - anon;

  // sexo
  sexo = document.getElementsByName("gen");
  if (sexo[0].checked) {
    sexo = "h";
  } else {
    sexo = "m";
  }

  // Estrutura Condicional
  if (idade == 0){
    content.innerHTML = 'Coloque a idade corretamente'
  } else if (idade <= 13 && sexo == "m") {
    content.innerText = `Detectamos uma menina de ${idade} anos.`;
    img.setAttribute("src", "imagens/crianca-m.jpg");
    content.appendChild(img);
  } else if (idade <= 21 && sexo == 'm'){
    content.innerText = `Detectamos uma moça de ${idade} anos.`;
    img.setAttribute("src", "imagens/adolescente-m.jpg");
    content.appendChild(img);
  } else if (idade <= 50 && sexo == 'm'){
    content.innerText = `Detectamos uma mulher de ${idade} anos.`;
    img.setAttribute("src", "imagens/adulto-m.jpg");
    content.appendChild(img);
  } else if (idade > 50 && sexo == 'm'){
    content.innerText = `Detectamos uma senhora de ${idade} anos.`;
    img.setAttribute("src", "imagens/idoso-m.jpg");
    content.appendChild(img);
  } else if (idade <= 13){
    content.innerText = `Detectamos um menino de ${idade} anos.`;
    img.setAttribute("src", "imagens/crianca-h.jpg");
    content.appendChild(img);
  } else if (idade <= 21){
    content.innerText = `Detectamos um jovem de ${idade} anos.`;
    img.setAttribute("src", "imagens/adolescente-h.jpg");
    content.appendChild(img);
  } else if (idade <= 50){
    content.innerText = `Detectamos um homem de ${idade} anos.`;
    img.setAttribute("src", "imagens/adulto-h.jpg");
    content.appendChild(img);
  } else{
    content.innerText = `Detectamos um senhor de ${idade} anos.`;
    img.setAttribute("src", "imagens/idoso-h.jpg");
    content.appendChild(img);
  }
  
}
