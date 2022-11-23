
from random import randint
from time import sleep

class bcolors:
    OK = '\033[92m' #green
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

itens= ('pedra', 'papel', 'tesoura')
computador = randint(0,2)


print('Suas opções são:\n[0]pedra\n[1]papel\n[2]tesoura')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!')
print('/' * 20)
print('Máquina jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('/' * 20)
#print('O computador escolheu {}'. format(itens[computador]))

if computador == 0:
    #computador jogou pedra
    if jogador == 0:
        print(bcolors.WARNING + 'Empate!😫' + bcolors.RESET)
    elif jogador ==1:
        print(bcolors.OK + 'Você Venceu..🥳' + bcolors.RESET)
    elif jogador ==2:
        print(bcolors.FAIL + 'VOCÊ PERDEU...😭' + bcolors.RESET)
    else:
        print('Jogada Inválida🤮')
#/////////////////////////////////////////////
elif computador == 1:
    #computador jogou PAPEL
    if jogador == 0:
        print(bcolors.OK +'Você Venceu..🥳' + bcolors.RESET)
    elif jogador ==1:
        print(bcolors.WARNING + 'Empate!😫' + bcolors.RESET)
    elif jogador ==2:
        print(bcolors.FAIL + 'VOCÊ PERDEU...😭' + bcolors.RESET)
    else:
        print('Jogada Inválida🤮')
#/////////////////////////////////////
elif computador == 2:
    #computador jogou TESOURA
    if jogador == 0:
        print(bcolors.FAIL + 'VOCÊ PERDEU...😭' + bcolors.RESET)
    elif jogador ==1:
        print(bcolors.OK + 'Você Venceu..🥳' + bcolors.RESET)
    elif jogador ==2:
        print(bcolors.WARNING + 'Empate!😫' + bcolors.RESET)
else:
    print('Jogada Inválida🤮')