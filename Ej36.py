while True:
    print("\n" + "="*40)
    print("  CALCULADORA CIENTÍFICA")
    print("="*40)
    print("1.  Suma")
    print("2.  Resta") 
    print("3.  Multiplicación")
    print("4.  División")
    print("5.  Potencia (x^y)")
    print("6.  Raíz cuadrada")
    print("7.  Raíz cúbica")
    print("8.  Factorial")
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("0.  Salir")
    print("="*40)
    
    option = input("Selecciona una opción: ")
    
    if option == '0':
        print("Fin")
        break
    
    elif option == '1':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        result = a + b
        print(f"Resultado: {a} + {b} = {result}")
    
    elif option == '2':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        result = a - b
        print(f"Resultado: {a} - {b} = {result}")
    
    elif option == '3':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        result = a * b
        print(f"Resultado: {a} × {b} = {result}")
    
    elif option == '4':
        a = float(input("Dividendo: "))
        b = float(input("Divisor: "))
        if b == 0:
            print("Error: No se puede dividir por cero")
        else:
            result = a / b
            print(f"Resultado: {a} ÷ {b} = {result}")
    
    elif option == '5':
        base = float(input("Base: "))
        exponent = float(input("Exponente: "))
        result = base ** exponent
        print(f"Resultado: {base}^{exponent} = {result}")
    
    elif option == '6':
        number = float(input("Número: "))
        if number < 0:
            print("Error: No se puede calcular raíz cuadrada de número negativo")
        else:
            if number == 0:
                result = 0
            else:
                x = number
                for _ in range(10):
                    x = (x + number / x) / 2
                result = x
            print(f"Resultado: √{number} = {result}")
    
    elif option == '7':
        number = float(input("Número: "))
        if number >= 0:
            result = number ** (1/3)
        else:
            result = -((-number) ** (1/3))
        print(f"Resultado: ∛{number} = {result}")
    
    
    elif option == '8':
        number = int(input("Número entero positivo: "))
        if number < 0:
            print("Error: El factorial solo está definido para números enteros no negativos")
        else:
            factorial = 1
            i = 1
            while i <= number:
                factorial *= i
                i += 1
            print(f"Resultado: {number}! = {factorial}")
    
    elif option == '9':
        angle = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angle > 2 * pi:
            angle -= 2 * pi
        while angle < -2 * pi:
            angle += 2 * pi
        
        sine = 0
        term = angle
        n = 1
        
        for i in range(15):
            sine += term
            term *= -angle * angle / ((n + 1) * (n + 2))
            n += 2
        
        print(f"Resultado: sen({angle:.4f}) = {sine:.6f}")
    
    elif option == '10':
        angle = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angle > 2 * pi:
            angle -= 2 * pi
        while angle < -2 * pi:
            angle += 2 * pi
        
        cosine = 1
        term = 1
        n = 0
        
        for i in range(15):
            term *= -angle * angle / ((n + 1) * (n + 2))
            cosine += term
            n += 2
        
        print(f"Resultado: cos({angle:.4f}) = {cosine:.6f}")
    
    elif option == '11':
        angle = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angle > 2 * pi:
            angle -= 2 * pi
        while angle < -2 * pi:
            angle += 2 * pi
        
        sine = 0
        term = angle
        n = 1
        
        for i in range(15):
            sine += term
            term *= -angle * angle / ((n + 1) * (n + 2))
            n += 2
        
        cosine = 1
        term = 1
        n = 0
        
        for i in range(15):
            term *= -angle * angle / ((n + 1) * (n + 2))
            cosine += term
            n += 2
        
        if cosine == 0:
            print("Error: Tangente no definida (coseno = 0)")
        else:
            tangent = sine / cosine
            print(f"Resultado: tan({angle:.4f}) = {tangent:.6f}")
    
    else:
        print("Opción no válida.")
    
    input("\nPresiona Enter para continuar...")
