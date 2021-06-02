'''
    Exemplo de menu interativo.
'''


# Menu principal
def menu_principal():
    print('> Menu principal:')
    print('1 - Escolher personagem')
    print('2 - Escolher mapa')
    print('3 - Escolher a dificuldade')
    print('4 - Carregar um jogo salvo')
    print('0 - Sair')
    x = int(input('\nEscolha uma opção: '))

    return x


# Opção 1
def menu_personagens():
    personagens = {
        1: 'Arqueiro',
        2: 'Bardo',
        3: 'Guerreiro',
        4: 'Ladino',
        5: 'Mago'
    }

    print('> Personagens:')
    for i in personagens:
        print(f'{i} - {personagens[i]}')
    print('0 - Voltar ao menu principal')

    escolha = int(input('\nEscolha um personagem: '))

    if escolha in personagens:
        print(f'\nVocê escolheu o personagem {personagens[escolha]}!')
        retorno = 99
    elif escolha == 0:
        retorno = 99
    else:
        print(f'\nPersonagem inválido!')
        retorno = 1

    return retorno


# Opção 2
def menu_mapas():
    mapas = {
        1: 'Caverna',
        2: 'Floresta',
        3: 'Montanha',
        4: 'Planície',
        5: 'Vale'
    }

    print('> Mapas:')
    for i in mapas:
        print(f'{i} - {mapas[i]}')
    print('0 - Voltar ao menu principal')

    escolha = int(input('\nEscolha um mapa: '))

    if escolha in mapas:
        print(f'\nVocê escolheu o mapa {mapas[escolha]}!')
        retorno = 99
    elif escolha == 0:
        retorno = 99
    else:
        print(f'\nMapa inválido!')
        retorno = 2

    return retorno


# Opções 3 e 4
def menu_em_desenvolvimento():
    print('> Menu em desenvolvimento')

    retorno = 99

    return retorno


# Verifica se o programa está sendo executado diretamente
if __name__ == '__main__':

    x = 99
    while x != 0:
        print('')
        print('-' * 20)

        if x == 99:
            x = menu_principal()
        elif x == 1:
            x = menu_personagens()
        elif x == 2:
            x = menu_mapas()
        elif x in (3, 4):
            x = menu_em_desenvolvimento()
        else:
            x = menu_principal()

        print('-' * 20)
