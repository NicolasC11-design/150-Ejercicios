import random
num = random.randint(1, 10)
adivinar = 0
while adivinar != num:
    adivinar = int(input('Adivina el número (1-10): '))
print('¡Correcto!')