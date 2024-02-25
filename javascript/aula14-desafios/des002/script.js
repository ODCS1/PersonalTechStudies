document.getElementById("botao").onclick = function () {
  let num = document.querySelector("input#itxt");
  let n = Number(num.value);
  let res = document.querySelector("select#seltab");
  if (num.value.length == 0) {
    window.alert("[ERRO] Coloque um valor válido");
  } else{
    res.innerHTML = ''
    for (var cont = 1; cont <= 10; cont++){
      let item = document.createElement('option')
      item.innerText = `${n} x ${cont} = ${n*cont}`
      item.value = 'res${cont}'
      res.appendChild(item)
    }
  }
};
