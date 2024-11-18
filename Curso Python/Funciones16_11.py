##Actividad 1 (Calcular promedio de notas)
def promediar(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    return promedio

print("Ingrese 3 notas para calcular su promedio")
not1=int(input("Nota 1:"))
not2=int(input("Nota 2:"))
not3=int(input("Nota 3:"))

resultado1=promediar(not1,not2,not3)
print(f"El promedio es: {resultado1}")

print("---------------------------------------------")
##Actividad 2 (Colores primarios)
print("¿Es primario el color (RGB)?")
def categorizar(rgb):
    if rgb=="rojo" or rgb=="azul" or rgb=="verde":
        print(f"El color {rgb} es primario.")
    else:
        print(f"El color {rgb} no es primario.")

col2=input("Ingrese un color:")
col3=col2.lower()
categorizar(col3)

print("---------------------------------------------")
##Actividad 3 (Número mayor de una serie de números)
def buscar_may(n1,n2,n3):
    if n1>n2 and n1>n3:
        may=n1
    elif n2>n1 and n2>n3:
        may=n2
    else:
        may=n3
    return may

print("Buscar el número mayor")
i1=int(input("Ingrese número 1:"))
i2=int(input("Ingrese número 2:"))
i3=int(input("Ingrese número 3:"))

resultado3=buscar_may(i1,i2,i3)

print(f"El número mayor es: {resultado3}")


print("---------------------------------------------")
##Actividad 4 (Crear rectangulo)
def hacer_rectangulo(fila,columna):
    print("* "*(columna))
    for i in range((fila-1)):
     print("* "*columna)
    
print("Dibuja un rectángulo")
f1=int(input("Ingresa tamaño de fila:"))
c1=int(input("Ingresa tamaño de columna:"))

hacer_rectangulo(f1,c1)

print("---------------------------------------------")
##Actividad 5 (Factorial)
def calcular_fac(num):
    ant=1
    for i in range (1,num+1):
        factorial=i*ant
        ant=factorial
    return factorial

num1=int(input("Ingrese un número para calcular su factorial:"))

resultado= calcular_fac(num1)

print(f"Factorial del número {num1}: {resultado}")
