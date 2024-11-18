import random

numero = random.randint (100, 200)
intentos = 0
intentos_maximos = 5

jugando = True

print("Adivina un numero del 100 al 200")

while jugando:
    intentos+=1
    
    if intentos <=5:
        eleccion = int(input("Elige un numero: "))
        if eleccion == numero:
            print("Acertaste, necesitaste", intentos, "intentos.")
            jugando = False
        elif eleccion > numero:
            print("Te pasaste, llevas", intentos, "intentos.")
        elif eleccion < numero:
            print("Demasiado bajo, llevas", intentos, "intentos.")
    else:
        print("Se acabaron los intentos, perdiste looser")
        jugando = False