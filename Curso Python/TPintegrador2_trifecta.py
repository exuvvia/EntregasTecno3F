n=input("Ingresar un número mayor a 0 para iniciar el programa:")
if not (n.isalpha()) and n.isdigit():
 n=int(n)
 while n>0:
     frase=input("Ingrese una palabra o frase:")
     print("Total de carácteres:",len(frase))
     num1=len(frase)
    
     aux=1
     for i in range (1,num1+1):
         factorial=i*aux
         aux=factorial
 
     print(f"Factorial de {num1}: {factorial}")
    
     poi=factorial%2
     if poi==0:
         print("El número es par")
     else:
         print("El número es impar")

     n=(input("Ingresar un número mayor a 0 para iniciar el programa:"))
     if not (n.isalpha()) and n.isdigit():
         n=int(n)
     else:
         break        
          
elif n.isalpha():
    breakpoint     