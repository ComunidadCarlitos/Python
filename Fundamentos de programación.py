a= 5 #entero
b= "3" #string
c= True #boolean
d= 0.5 #float
e= 0.3j #complex

#verificando el tipo de dato
print("Tipos de datos iniciales")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#verificando el tipo de dato
print("Tipos de datos modificados")
print(type(str(a)))
print(type(int(b)))
print(type(int(c)))
print(type(str(d)))

#Planteamiento del reto tema 1
salario=float(input("Escriba cuál es su salario: "))
alimentos=salario*0.22
pasajes=salario*0.17
cine=salario*0.12
libros=salario*0.10
alquiler=(salario-alimentos-pasajes-cine-libros)
print("El valor restante del salario para el pago del alquiler es el siguiente:", round(alquiler,3))


nombre=input("Escriba su nombre: ")
print("Ahora estás en la matrix," + " "+nombre)

year_nacimiento=1998
year_nacimiento=2021-year_nacimiento
print("La edad es: ",(year_nacimiento))

#Multiplicacion
a=5
b=6
c=a*b
print(a*b)
print(c)
print(5*6)

#Division
a=5
b=6
c=a/b
print(a/b)
print(c)
print(5/6)
print(5//6)

#Ejerciciotarea
a=int(input("Escriba el valor para a: "))
b=int(input("Escriba el valor para b: "))
suma= a+b
print(suma)
c=int(input("Escriba el valor para una nueva variable c: "))
print(suma*c)

#CLASE07052021

#Acumulado de notas y promedio
nota1=float(input ("Escribir nota número 1: "))
nota2=float(input ("Escribir nota número 2: "))
nota3=float(input ("Escribir nota número 3: "))
nota4=float(input ("Escribir nota número 4: "))
notatotal=(nota1*0.2+nota2*0.3+nota3*0.25+nota4*0.25)
print("La nota definitiva es: "+ str(notatotal))


#Peso de una persona
peso=float(input("Escriba su peso en KG: "))
altura=float(input("Escriba su estatura en metros: "))
IMC=(peso/altura**2)
IMC1=round(IMC,2)
print("Tu indice de masa corporal es: ", IMC1)

#Saber si la división es exacta o no
n1=int(input("Escriba un número entero:"))
n2=int(input("Escriba otro número entero: "))
if n2==0:
    print("n2 tiene que ser diferente de 0")
    n2=int(input("Escriba el nuevo valor para n2: "))
n3=(n1/n2)
if (n1%n2)==0:
    print("La división es exacta", n3)
else:
    print("La división no es exacta",round(n3,3))


#Saber si un número es mayor que otro 
n1=int(input("Escriba un número: "))
n2=int(input("Escriba un número: "))
if n1==n2:
    print("n1 es igual a n2 \nn1=", n1)
elif n1>n2:
    print("n1 es el número mayor: "+str(n1) +"\n"+ "n2 es el número menor: "+ str(n2))
else:
    print("n2 es el número mayor: "+ str(n2)+"\n"+ "n1 es el número menor: " + str(n1))


#Saber si he escrito varias veces X número
n1= int(input("Escriba un número: "))
n2= int(input("Escriba un número: "))
n3= int(input("Escriba un número: "))
if n1==n2 and n2==n3:
    print("Ha escrito 3 veces el mismo número")
elif n1==n2 or n1==n3 or n2==n3:
    print("Ha escrito 2 veces el mismo número")
else:
    print("Todos los números son diferentes")

#Conversión de unidades
cm=float(input("Escriba una distancia en cm: "))
m=(cm/100)
km=(cm/100000)
if km>=1 and m>=1:
    print("La distancia en Km es: "+str(round(km,3))+"\n"+"La distancia en M es: "+str(round(m,3))+"\n"+"La distancia en cm es: "+str(cm))
elif m>=1 and cm>=1:
    print("La distancia en cm es: "+str(cm)+"\n"+"La distancia en M es: "+str(round(m,3)))
else:
    print("La distancia en cm es: "+str(cm))

#Suma de entero y flotante
n=float(input("Ingrese un número con decimales: "))
m=int(input("Ingrese un número entero: "))
suma=(n+m)
print("El resultado de la suma es", suma)

#Promedio
a=int(input("Escriba un número: "))
b=int(input("Escriba un número: "))
c=int(input("Escriba un número: "))
print((a+b+c)/3)

#Sacar el 15% de un número
n=int(input("Escriba un número: "))
print(n-0.15)

#Ejercicio profe
n=int(input("Escriba un número: "))
m=int(input("Escriba otro número: "))
if n==m:
    print("Son iguales")
elif n!=m and n>m:
    print("Son diferentes y el primer número es mayor que el segundo")
else:
    print("Son diferentes y el segundo número es mayor que el primero")

