def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if b != 0: 
        resultado = a / b
        return resultado
    else:
        return "Error: No se puede dividir entre cero"
num1 = 20
num2 = 5

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("-" * 30)
print(f"{num1} + {num2} = {sumar(num1, num2)}")
print(f"{num1} - {num2} = {restar(num1, num2)}")
print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
print(f"{num1} / {num2} = {dividir(num1, num2)}")
print(f"{num1} / 0 = {dividir(num1, 0)}")