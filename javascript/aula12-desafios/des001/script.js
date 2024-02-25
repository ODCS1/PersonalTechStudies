function carregar() {
  var msg = window.document.querySelector("div#msg");
  var img = window.document.querySelector("img#imagem");
  var agora = new Date();
  var hora = agora.getHours();
  if (hora >= 0 && hora < 12) {
    msg.innerText = `Agora são ${hora} horas, tenha uma boa manhã.`;
    img.src = 'manha.jpg'
    document.body.style.background = '#e2cd9f'
  } else if (hora >= 12 && hora < 18) {
    msg.innerText = `Agora são ${hora} horas, tenha uma boa tarde.`;
    img.src = 'tarde.jpg';
    document.body.style.background = '#b9846f'
  } else {
    msg.innerText = `Agora são ${hora} horas, tenha uma boa noite.`;
    img.src = 'noite.jpg';
    document.body.style.background = '#515154'
  }
}
