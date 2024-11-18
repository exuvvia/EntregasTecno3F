import random
numrandom=random.randint(1,50)

f=0
g=1
print("JUEGO: ADIVINA EL NÚMERO DE 1 A 50")

while f<5 and g!=5:
 num=int(input("Ingresar número:"))
 if num<numrandom:
    f+=1
    print("INCORRECTO, ES UN NÚMERO MAYOR")
  
 elif num>numrandom:
    f+=1
    print("INCORRECTO, ES UN NÚMERO MENOR")

 else:
    g=5

if f==5:
  print(f"PERDISTE EL JUEGO, EL NÚMERO ES {numrandom}")
elif g==5:
  print("GANASTE EL JUEGO")