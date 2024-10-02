import os

os.system('cls')

# EXEMPLO [1]
# nome = input('Informe o seu nome: ')
# nota1 = float(input('Informe a nota 1: '))
# nota2 = float(input('Informe a nota 2: '))

# soma = nota1 + nota2 
# med = soma /2

# tupla_notas = (nome, nota1, nota2, med)

# print(f'Dados do Usuário: {tupla_notas}')


# ATIVIDADE [1]
nome = input('Informe o seu nome: ')
cargo = input('Informe a seu cargo: ')
salario = float(input('Informe o seu salário: '))
idade = int(input('Informe a sua idade: '))

tupla_cadastro = (nome, cargo, salario, idade)

print(f'Cadastro de cliente: {tupla_cadastro}')