multiplos_3_5 = []

for numero in range(1,1000,1):
    if numero % 3 == 0:
        multiplos_3_5.append(numero)
    elif numero % 5 == 0:
        multiplos_3_5.append(numero)

print(sum(multiplos_3_5))