import os

os.system('cls')

# ATIVIDADES [1]

# usuario digita 2 numeros, saber se é par ou não

# def solucao(txt):
#     num = n1 %2
#     if num == 0:
#         print('Número par')
#     else:
#         print('Número Ímpar')
    


# n1 = int(input('Número: '))

# solucao(n1)



def verifica_par(n):
    resposta = ''
    valor = n1 % 2
    if valor == 0:
        resposta = 'Par'
    else:
        resposta = 'Ímpar'
    return resposta


n1 = int(input('Número: '))

resp = verifica_par(n1)
print(f'{n1} é {resp}')


