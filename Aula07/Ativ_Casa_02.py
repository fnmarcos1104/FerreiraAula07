import os

os.system('cls')


# clima = ['Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado', 'Ensolarado']
# dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

# dias_ensolarados = []
# dias_sem_sol = []

# for i in range(len(clima)):
#     if clima[i] == "Ensolarado":  # Verifica se o dia é ensolarado
#         dias_ensolarados.append(dias[i])  # Adiciona o dia à lista de ensolarados
#     else:  # Caso contrário, é um dia sem sol
#         dias_sem_sol.append(dias[i])  # Adiciona o dia à lista de sem sol

# print("Dias Ensolarados:")
# for dia in dias_ensolarados:
#     print(dia)  # Mostra os dias ensolarados

# print("\nDias Sem Sol:")
# for dia in dias_sem_sol:
#     print(dia)  # Mostra os dias sem sol

clima = ['Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado', 'Ensolarado']
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

dias_ensolarados = []
dias_sem_sol = []

# for i in clima:
#     if i == "Ensolarado":  
#         dias_ensolarados.append(i) 
#     else:  
#         dias_sem_sol.append(i)  

# print(f"Dias Ensolarados: {dias_ensolarados}")

# print(f"\nDias Sem Sol: {dias_sem_sol}")



for i, v in enumerate(clima):
    if clima[i] == 'Ensolarado':
        dias_ensolarados.append(dias[i])
    else:
        dias_sem_sol.append(dias[i])

print(f"Dias Ensolarados: {dias_ensolarados}")

print(f"\nDias Sem Sol: {dias_sem_sol}")
