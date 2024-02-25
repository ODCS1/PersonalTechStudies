function contar() {
  // Mensagem
  let msg = document.querySelector("div#res");

  // Contar
  let inicio = document.querySelector("input#istart");
  let fim = document.querySelector("input#iend");
  let passo = document.querySelector("input#ipasso");

  // Estruturas que vão ter um resultado na tela

  if (inicio.value == 0 && fim.value == 0 || passo.value == 0) {
    window.alert("[ERRO] tente novamente");
  } else {
    msg.innerHTML = "Contando: ";
    let i = Number(inicio.value);
    let f = Number(fim.value);
    let p = Number(passo.value);
    if (i < f && p > 0) {
      for (var c = i; c <= f; c += p) {
        msg.innerHTML += `${c} \u{1F449}`;
        if (c == f){
          msg.innerHTML += ` FIM! \u{1F3C1}`;
        }
      }
    } else if (i > f) {
      for (c = i; c >= f; c -= p) {
        msg.innerHTML += `${c} \u{1F449}`;
        if (c == f){
          msg.innerHTML += ` FIM! \u{1F3C1}`;
        }
      }
    }
  }
}
