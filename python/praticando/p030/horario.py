def ano_novo(horario: str)-> str:
    hora, minuto, segundo = horario.split(':')
    hora = int(hora) if hora[0] != '0' else int(hora[1])
    minuto = int(minuto) if minuto[0] != '0' else int(minuto[1])
    segundo = int(segundo) if segundo[0] != '0' else int(segundo[1])

    segundos_total = 60 - segundo  
    minutos_total = 60 - minuto   #  
    hora_total = 24 - hora

    # if minutos_total == 0: 09 + 10
    #     minutos_total = 60

    if segundos_total > 0:
        minutos_total -= 1

        
    if minutos_total > 0 :
        hora_total-= 1
    
    

    return f'{hora_total:02d}:{minutos_total:02d}:{segundos_total:02d}'

print(ano_novo('10:00:00'))


'''
22:59:50

00:00:10 = 23:59:50

24:60:60


'''