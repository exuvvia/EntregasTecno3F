#Actividad 1 (Num par o impar)

num=int(input("Ingresar un número:"))
if (num % 2 != 0):
   print("El número es impar")
else:
   print("El número es par")


print("------------------------------")

#Actividad 2 (Tabla de multiplicar)
num2=int(input("Ingrese un número para ver su tabla:"))
for i in range (0,10):
   print(f"{num2} * {i+1} = {(i+1)*num2}")


print("------------------------------")


#Actividad 3 (Mayor de edad)
nombre=input("Ingrese su nombre:")
edad=int(input("Ingrese su edad:"))
if edad>=18:
   print("Sos mayor de edad")
else:
   print("Sos menor de edad")


print("------------------------------")   

#Actividad 4 (Palabra x número ingresado)
palabra=input("Ingrese una palabra:")
num3=int(input("Ingrese un número:"))
for j in range(0,num3):
   print(palabra)

print("------------------------------")

#Actividad 5 (Sumar números hasta el ingreso de 0)
contador=1
total=0
while contador!=0:
   num4=int(input("Ingrese un número:"))
   total+=num4
   if num4==0:
      contador=0
   
print(f"El total de la suma es de: {total}")

print("------------------------------")