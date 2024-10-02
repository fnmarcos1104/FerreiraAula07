import os

os.system('cls')

def decoracao():
    print()
    print(30*'=')


def saudacao(txt):
    print(f'Olá {txt}!')


def somar_valores(a, b):
    total = a + b
    med = (a + b) /2
    # print(f'O total é {total}.')
    return total, med


# decoracao()
# print('Iniciando Programa')
# print('nome: ')
# print('idade: ')
# print('cidade: ')

# decoracao()
# print('Dados Pessoais')
# print('CPF: ')
# print('RG: ')

# decoracao()
# print('Rede Social')
# print('Linkedin')
# print('GitHub')


# print('INICIANDO O PROGRAMA')
# nome = input('Informe o seu nome: ')

# saudacao(nome)

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

valor, media = somar_valores(n1, n2)

print(valor, media)

