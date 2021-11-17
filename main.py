from os import system, name # importa informações sobre o sistema operacional em uso
import funcoes
dia = 0
mes = 0



def clear(): # limpa a tela removendo do prompt as informações sobre a localização dos arquivos
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def seleciona_signo():
    stop = False              
    while stop == False:
        
        if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
            signo = 'Áries'
            stop = True
        elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
            signo = 'Touro'
            stop = True
        elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
            signo = 'Gêmeos'
            stop = True
        elif (dia >= 21 and mes == 6) or (dia <= 20 and mes == 7):
            signo = 'Câncer'
            stop = True
        elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
            signo = 'Leão'
            stop = True
        elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
            signo = 'Virgem'
            stop = True
        elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
            signo = 'Libra'
            stop = True
        elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
            signo = 'Escorpião'
            stop = True
        elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
            signo = 'Sagitário'
            stop = True
        elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
            signo = 'Capricórnio'
            stop = True
        elif (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
            signo = 'Aquário'
            stop = True
        elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
            signo = 'Peixes'
            stop = True
    print(nome +' sua data de aniversário é '+ str(dia) + '/' + str(mes) + ' e seu signo é: '+ signo) 

clear()

stop = False

while stop == False:
    nome = input('Por favor informe seu nome: ')
    dia = int(input('Informe o seu dia de nascimento: '))
    print('Por favor, digite o número do seu mês de nascimento, considerando: ')
    print('=' * 95)
    print('\n Janeiro =   1 '
    '\n Fevereiro = 2'
    '\n Março =     3'
    '\n Abril =     4'
    '\n Maio =      5'
    '\n Junho =     6'
    '\n Julho =     7'
    '\n Agosto =    8'
    '\n Setembro =  9'
    '\n Outubro =   10'
    '\n Novembro =  11'
    '\n Dezembro =  12'
    '\n')
    mes = int(input('Digite o número correspondente ao seu mês de nascimento: '))    

    clear()
    print('=' * 95 )
    seleciona_signo()
    print('=' * 95 )
    print('=' * 20 + '  HORÓSCOPO DO DIA PARA OS NASCIDOS COM O SIGNO ACIMA:  ' + '=' * 18 +
    '\n')
    funcoes.gerador_de_lero_lero()
    print('\n')

    continua = input('Deseja jogar novamente? ')
    if continua == 'S' or continua == 's':
        clear()
        stop = False
    else:
        stop = True
        exit()