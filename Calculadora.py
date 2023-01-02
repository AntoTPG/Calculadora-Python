#Calcuradora
print("CALCULADORA \n")
user_name = input("Bienvenido a la calculadora, ingrese su nombre: ")
print(user_name,"puede usar la calculadora")
print("Estas son las operaciones que puede realizar: Suma - Resta - Multiplicación - División")
operacion = input("escriba que operación quiere hacer:")
print("Perfecto, vamos a realizar una", operacion)

if operacion == "suma" or "Suma":
    sumando_1 = int(input("Introduzca el primer sumando: "))
    sumando_2 = int(input("Introduzca el segundo sumando: "))
    resultado = sumando_1 + sumando_2
    print("El resultado de la suma es: ", resultado)
elif operacion == "resta" or "Resta":
    minuendo = int(input("Introduzca el minuendo: "))
    sustraendo = int(input("Introduzca el sustraendo: "))
    diferencia = minuendo - sustraendo
    print("El resultado de la resta es: ", diferencia)
elif operacion == "multiplicación" or "multiplicacion":
    factor_1 = int(input("Introduzca el primer factor: "))
    factor_2 = int(input("Introduzca el segundo factor: "))
    producto = round(factor_1 * factor_2)
    print("El producto de la multiplicación es: ", producto)
elif operacion == "division" or "división":
    dividendo = int(input("Introduzca el dividendo: "))
    divisor = int(input("Introduzca el divisor "))
    cociente = round(dividendo / divisor)
    resto = dividendo % divisor
    print("El cociente de la división es: ", cociente)
    print("El resto de la división es: ",resto)
else:
    print("Operación no Válida")