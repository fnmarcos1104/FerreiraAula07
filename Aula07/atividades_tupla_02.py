import os

os.system('cls')

# ATIVIDADE [2]

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
n5 = int(input('Digite o quinto numero: '))

tupla = (n1, n2, n3, n4, n5)

maior = (max(tupla))
menor = (min(tupla))
soma = (sum(tupla))


print(f'O maior número é: {maior}, o menor número é: {menor} e a soma dos números é: {soma}.')
print (sorted(tupla))
