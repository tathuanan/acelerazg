import math

def primo(numero_testado):
    for numero in range(2, math.floor(math.sqrt(numero_testado)) + 1):
        if numero_testado % numero == 0:
            return False
    return True

def maior_fator_primo(numero_testado):
    fatores = []
    for numero in range(2, math.floor(math.sqrt(numero_testado)) + 1):
        if primo(numero):
            if numero_testado % numero == 0:
                fatores.append(numero)
    return sorted(fatores)[-1]

print(maior_fator_primo(600851475143))