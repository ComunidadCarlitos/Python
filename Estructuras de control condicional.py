"""precio=int(input("Escriba el precio de cada docena: "))
p=int(input("Escriba la cantidad de docenas del producto deseado: "))
if p>3:
    preciod=(precio-precio*0.15)
    p1=(p-3)
    print("El costo total de las: "+str(p)+ " docenas, es de: "+str(precio*p))
    print("El descuento obtenido fue de: "+str((precio*0.15)*p)+"\n"+"El monto a pagar incluyendo el descuento es: "+str(p*preciod))
    print("El número de docenas compradas fueron: "+str(p)+" es decir, "+str(p*12)+" unidades, se le obsequió "+str(p1)+" unidad por comprar más de 3 docenas, en total se lleva: "+str(p1)+ " unidades")
else:
    precion=(precio-precio*0.10) 
    print("El costo total de las: "+str(p)+ " docenas, es de:"+str(precio*p))
    print("El descuento obtenido fue de: "+str((precio*0.10)*p)+"\n"+"El monto a pagar incluyendo el descuento es: "+str(p*precion))
    print("El número de docenas compradas fueron: "+str(p)+" es decir, "+str(p*12)+" unidades")
    
n=int(input("Escriba un numero: "))
if n%2==0:
    if n>0:
        print("El número es par positivo")
    else:
        print("El número es par negativo")
else:
    print("El número no es par")

n=float(input("Ingrese las horas utilizadas: "))
m=float(input("Ingrese los minutos utilizados: "))
if m>=1:
    n=n+1
    pago=n*1500
    print("El valor a pagar es: ", pago)
else:
    pago=n*1500
    print("El valor a pagar es: ", pago)

#Ejercicio en clase
x=int(input("Escriba el valor de X: "))
y=int(input("Escriba el valor de Y: "))
if x>0 and y>0:
    print("Está en el cuadrante I")
elif x<0 and y>0:
    print("Esta en el cuadrante II")
elif x<0 and y<0:
    print("Está en el cuadrante III" )
elif x>0 and y<0:
    print("Está en el cuadrante IV")
else:
    print("Está en el origen")
    
#Unidades de temperatura
t=float(input("Escriba los grados a convertir: "))
t1=input("Escriba las unidades de la temperatura: ")
if t1=="°C":
    f=(9*t+(32*5))/5
    print("La temperatura convertida es: "+str(f)+" °F")
elif t1=="°F":
    c=(5*(t-32))/9
    print("La temperatura es: "+str(c)+" °C")
else:
    print("La temperatura dada no es en grados Celsius o Fahrenheit") """
    

"""print("A continuación ingrese un número de 3 cifras dividido por centenas, decenas y unidades.")
centena=int(input("Ingrese el número de la centena: "))
decena=int(input("Ingrese el número de la decena: "))
unidades=int(input("Ingresa el número de la unidad: "))
if unidades==centena:
    print("El número es igual si se lee al contrario")
    print(str(centena)+str(decena)+str(unidades))
else: 
    print("El número no se lee igual al revés")

print("A continuación ingrese un número de 3 cifras dividido por centenas, decenas y unidades.")
centena=int(input("Ingrese el número de la centena: "))
decena=int(input("Ingrese el número de la decena: "))
unidades=int(input("Ingresa el número de la unidad: "))
if centena/unidades==1:
    print("El número es igual si se lee al contrario")
    print(str(centena)+str(decena)+str(unidades))
else: 
    print("El número no se lee igual al revés")"""


"""Ejercicio1
num=int(input("Ingrese el número de 3 cifras: "))
centena=(num//100)
decena=(num%10)
if centena==decena:
    print("El número es igual si se lee al contrario")
    print(num)
else: 
    print("El número no se lee igual al revés")

#Ejercicio2
x=int(input("Escriba los kilómetros recorridos: "))
if x<=300:
    precio=300000
    precio1=precio/1.2
    print("El monto a pagar a pagar por el alquiler del vehículo es: "+str(precio-precio1)+"el monto total es: "+str(precio))
elif x>300 and x<=1000:
    x1=(x-300)/100
    precio=300000+15000*x1
    precio1=precio/1.2
    print("El monto a pagar a pagar por el alquiler del vehículo es: "+str(precio-precio1)+" el monto total es: "+str(precio))
elif x>1000:
    x1=(x-300)/100
    precio=300000+15000*x1
    x2=(x-1000)/1000
    precio2=10000*x2
    preciototal=precio+precio2
    preciototal2=preciototal/1.2
    print("El monto a pagar a pagar por el alquiler del vehículo es: "+str(preciototal-preciototal2)+" el monto total es: "+str(preciototal))"""

nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
nota4=float(input("Ingrese la cuarta nota: "))
if nota1!=nota2!=nota3!=nota4:
    if nota1>=nota2>=nota3>nota4 or nota1>=nota3>=nota2>nota4 or nota2>=nota1>=nota3>nota4 or nota2>=nota3>=nota1>nota4 or nota3>=nota1>=nota2>nota4 or nota3>=nota2>=nota1>nota4:
        notaf=(nota1+nota2+nota3)/3
        print("La nota eliminada fue: "+str(nota4)+" y la nota final es: "+str(notaf))
    elif nota2>=nota3>=nota4>nota1 or nota2>=nota4>=nota3>nota1 or nota3>=nota2>=nota4>nota1 or nota3>=nota4>=nota2>nota1 or nota4>=nota2>=nota3>nota1 or nota4>=nota3>=nota2>nota1:
        notaf=(nota4+nota2+nota4)/3
        print("La nota eliminada fue: "+str(nota1)+" y la nota final es: "+str(notaf))
    elif nota3>=nota4>=nota1>nota2 or nota3>=nota1>=nota4>nota2 or nota1>=nota4>=nota3>nota2 or nota1>=nota3>=nota4>nota2 or nota4>=nota3>=nota1>nota2 or nota4>=nota1>=nota3>nota2:
        notaf=(nota4+nota2+nota4)/3
        print("La nota eliminada fue: "+str(nota2)+" y la nota final es: "+str(notaf))
    elif nota4>=nota1>=nota2>nota3 or nota4>=nota2>=nota1>nota3 or nota1>=nota2>=nota4>nota3 or nota1>=nota4>=nota2>nota3 or nota2>=nota1>=nota4>nota3 or nota2>=nota4>=nota1>nota3:
        notaf=(nota4+nota2+nota4)/3
        print("La nota eliminada fue: "+str(nota3)+" y la nota final es: "+str(notaf))    
else:
    notaf=(nota1+nota2+nota3+nota4)/4
    print("Las notas se repiten 4 veces, por ende la nota promedio es: ", notaf)
        
"""#2 Ejercicio
l=int(input("Escriba el valor del lado 1: "))
m=int(input("Escriba el valor del lado 2: "))
n=int(input("Escriba el valor del lado 3: "))
if (l+m)>n and (l+n)>m and (m+n)>l:
    if l==m==n:
        print("Es un triángulo equilátero")
    elif l==m or l==n or m==n:
        print("Es un triángulo iósceles")
    else:
        print("Es un triángulo escaleno")
else:
    print("No es triángulo")"""
