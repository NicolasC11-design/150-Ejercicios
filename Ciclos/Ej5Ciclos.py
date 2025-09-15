n = 123456
suma = 0
while n > 0:
    suma += n % 10
    n //= 10
print(suma)