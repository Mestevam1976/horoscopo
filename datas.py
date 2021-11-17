import main
dia = main.dia_de_nascimento
mes = main.mes_numerico

# Áries: de 21 de março a 20 de abril;

# Touro: de 21 de abril a 20 de maio;

# Gêmeos: de 21 de maio a 20 de junho;

# Câncer: de 21 de junho a 22 de julho;

# Leão: de 23 de julho a 22 de agosto;

# Virgem: de 23 de agosto a 22 de setembro;

# Libra: de 23 de setembro a 22 de outubro;

# Escorpião: de 23 de outubro a 21 de novembro;

# Sagitário: de 22 de novembro a 21 de dezembro;

# Capricórnio: de 22 de dezembro a 20 de janeiro;

# Aquário: de 21 de janeiro a 18 de fevereiro;

# Peixes: de 19 de fevereiro a 20 de março

def seleciona_signo():
    if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
        signo = 'Áries'
    elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
        signo = 'Touro'
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        signo = 'Gêmeos'
    elif (dia >= 21 and mes == 6) or (dia <= 20 and mes == 7):
        signo = 'Câncer'
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        signo = 'Leão'
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        signo = 'Virgem'
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        signo = 'Libra'
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        signo = 'Escorpião'
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        signo = 'Sagitário'
    elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
        signo = 'Capricórnio'
    elif (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
        signo = 'Aquário'
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        signo = 'Peixes'
    
    print(signo)

a = len('texto')
