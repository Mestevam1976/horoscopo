import random, messages


def escolher_cor(cor, texto): # função para definir as cores das mensagens
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'

def gerador_de_lero_lero():

    aleatorio = random.randrange(1,12)

    if aleatorio == 1:
        texto = messages.message_01
        print(escolher_cor('red', texto))
    elif aleatorio == 2:
        texto = messages.message_02
        print(escolher_cor('red', texto))
    elif aleatorio == 3:
        texto = messages.message_03
        print(escolher_cor('red', texto))
    elif aleatorio == 4:
        texto = messages.message_04
        print(escolher_cor('red', texto))
    elif aleatorio == 5:
        texto = messages.message_05
        print(escolher_cor('blue', texto))
    elif aleatorio == 6:
        texto = messages.message_06
        print(escolher_cor('blue', texto))
    elif aleatorio == 7:
        texto = messages.message_07
        print(escolher_cor('blue', texto))
    elif aleatorio == 8:
        texto = messages.message_08
        print(escolher_cor('blue', texto))
    elif aleatorio == 9:
        texto = messages.message_09
        print(escolher_cor('yellow', texto))
    elif aleatorio == 10:
        texto = messages.message_10
        print(escolher_cor('yellow', texto))
    elif aleatorio == 11:
        texto = messages.message_11
        print(escolher_cor('yellow', texto))
    elif aleatorio == 12:
        texto = messages.message_12
        print(escolher_cor('yellow', texto))





    
    
