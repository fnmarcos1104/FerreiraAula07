import os

os.system('cls')

tupla_vazia = ()

# Tupla de um elemento
tupla_um_elemento = (10,)
# print(tupla_um_elemento)
# print(type(tupla_um_elemento))

# Tupla de vários elementos
tupla_varios_elementos = (5, 4, 10, 15, 12)
print(tupla_varios_elementos)


tupla = (10, 20, 30)
print(tupla[0])


print(tupla[1:4])

tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos
print(tupla_um_elemento)

print(10 in tupla_varios_elementos)

print (sorted(tupla_varios_elementos))
