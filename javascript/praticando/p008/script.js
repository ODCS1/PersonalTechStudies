function agora(){
  let horario = new Date().getHours()
}

if (horario >= 0 && horario < 12){
  alert('img dia')
}else if (horario >= 12 && horario < 18){
  alert('img trde')
}else if (horario >= 18 && horario < 24){
  alert('img noitr')
}

for(let c = 1; c <= horario; c++){
  alert(`${c} + ${horario} = ${(c * horario) - 1}`)
}
