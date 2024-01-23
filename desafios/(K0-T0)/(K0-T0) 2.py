fibonacci = [1,2]
termos_pares = []

while True:
    soma = fibonacci[-1] + fibonacci [-2]
    if soma > 4000000:
        break
    else:
        fibonacci.append(soma)
    
for numero in fibonacci:
    if numero % 2 == 0:
        termos_pares.append(numero)

print(sum(termos_pares))
