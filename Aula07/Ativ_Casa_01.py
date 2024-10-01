import os

os.system('cls')

n1 = float(input('Digite a primera nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

nf = n1 + n2 + n3 + n4 
md = nf / 4

print(md)

if md >= 7:
    print('ALUNO APROVADO')
elif md >= 5:
    print('ALUNO EM RECUPERAÇÃO')
else:
    print('ALUNO REPROVADO')


