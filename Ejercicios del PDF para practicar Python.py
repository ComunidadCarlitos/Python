#Escribir un programa que solicite un valor entero al usuario y determine si es par o impar
"""num=int(input("Escriba un número: "))
if num%2==0:
    print("El número es par: ",num)
else:
    print("El número es impar: ",num)

#Programa que determine si número es par o impar

num2=int(input("Escriba un número: "))
if num2>0:
    print("Número es positivo")
else:
    print("Número negativo")
    
#programa que pida un número y si es positivo pida otro valor, sume, reste y multiplique.
num3=int(input("Escriba un número: "))
if num3>0:
    num4=int(input("Ingrese otro número: "))
    suma=num3+num4
    resta=num3-num4
    producto=num3*num4
    print("suma: ",suma," resta: ",resta," multiplicación: ",producto)
else:
    print("No es positivo el número.")

#Calcular el número mayor de 2 números
num5=int(input("Escriba el primer número: "))
num6=int(input("Escriba el segundo número: "))
if num5>num6:
    print("El número mayor es el primer número ",num5)
else:
    print("El número mayor es el segundo número: ",num6)

numeros=[]
pregunta=int(input("Cuántos números va a ingresar? "))
while pregunta!=0:
    for i in range (0,pregunta):
        numero=int(input("Ingrese un número: "))
        numeros.append(numero)
    print("el número mayor es: ",max(numeros))
    pregunta=int(input("Cuántos números va a ingresar? "))
    
#Determinar en qué estado está el agua con la temperatura
Temp=int(input("Escriba la temperatura del agua: "))
if Temp<0:
    print("Su estado es sólido")
elif 0<Temp<=100:
    print("Su estado es líquido")
else:
    print("Su estado es gaseoso")

#Hacer un programa que calcula la fecha del día siguiente dada una fecha dada
dia=int(input("Ingrese el día "))


#Escriba un programa que solicite la cantidad a ahorrar y que haga suma hasta que el ahorro se complete
ahorro=int(input("Ingrese la cantidad de dinero que desea ahorrar: "))
faltante=ahorro
while faltante!=0:
    suma=int(input("¿Qué cantidad de dinero desea añadir?: "))
    faltante=faltante-suma
    if faltante<=0:
        print("Cumplió su objetivo de ahorro", ahorro)
        
        
        el=input("¿Cuál es el nombre de la persona que amará: ")
while el  !="Jhon":
    print("Solo puede ser Jhon \n")
    el=input("¿Cuál es el nombre de la persona que amará: ")
if el=="Jhon":
    respuesta= input("¿Dará atención? :")
    respuesta2= input ("¿Dará cariñitos?: ")
    if respuesta=="Sí" and respuesta2=="Sí":
            print("Será de Paula")
    elif respuesta=="Sí" or respuesta2=="Sí":
            print("Le falta uno para ser de Paula")
    else:
            print("Nunca será de Paula")
"""""

#Escriba un programa para una heladería

print("Hola, muy buenos días, bienvenido a su heladería La Favorita"+"\n")
resp=input("¿Desea comprar un helado sencillo?: " )
toppings={'Oreo':1, 'KiKat':1.50, 'Brownie':0.75, 'Lacasitos':0.95}
if resp=="sí" or resp=="si":
    print("El precio de su helado es 1.90 euros")
else:
    top=input("¿Cuál es su topping deseado?: ")
    if top in toppings:
        valor=float(toppings.get(top,"El sabor no lo tenemos, intente con otro"))
        print("El valor del helado sería: ",round((1.90+valor),3), "euros")
        