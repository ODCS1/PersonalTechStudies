/*  Escreva um progema em javascript para simular uma fila de espera em um consultório médico. O programa deve iniciar na tela de um menu interativo contendo a lista de todos os pacientes esperando em ordem mostrando sua posição ao lado do nome (ex: 1° Matheus, 2° Marcos, etc). O menu também deve permitir escolher entre as opções de "Novo paciente", para adicionar um novo paciente ao fim da fila (pedindo o nome do paciente), "Consultar paciente", que retira o primeiro paciente da fila e mostra na tela o nome do paciente consultado, e "Sair". O programa só deve ser encerrado ao escolher a opção de "Sair", caso contrário deve voltar ao menu.
*/



















let nomes = []
let opcao = ''
let pacientes = ''
do{
  for(let i = 0; i < length(nomes); i++){
    pacientes += `${(i+1)}º - ${nomes[i]} \n`
  }
  opcao = prompt(`Fila: ${pacientes} \n
  [1] Novo paciente \n
  [2] Consultar paciente \n
  [3] Sair \n
  `)

  switch (opcao){
    case "1":
      novo_paciente = prompt('Digite o nome do novo paciente: ')
      nomes.push(novo_paciente)
      break
    case "2":
      let pacienteConsultado = nomes.shift()
      alert(`${pacienteConsultado} foi removido da lista.`)
      break
    case "3":
      alert('SAINDO . . .')
      break
    default:
      alert('Escolha uma opção válida!')
  }

}while(opcao != 3)