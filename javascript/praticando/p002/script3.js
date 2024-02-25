
    // function saudacao(){
    //   alert('Olá, boa noite a todos!')
    //   nome = prompt('Diga o seu nome: ')
    //   alert(`O seu nome é ${nome}!`)
    //   resposta = confirm('Deseja realmente aprender JS? ')
    //   if (resposta == 'ok'){
    //     alert('Maravilha, vamos começar!')
    //   }else{
    //     alert('Que pena, até a próxima...')
    //   }
    // }

    function clicou(){
      ano_nasc = Number(prompt('Digite a sua data de nascimento: '))
      idade = 2023 - ano_nasc
      if (idade < 5){
        alert(`Idade não compatível.`)
      }else{
        alert(`Como você nasceu no ano de ${ano_nasc}, você possuí ${idade} anos de idade.`)
      }
    }